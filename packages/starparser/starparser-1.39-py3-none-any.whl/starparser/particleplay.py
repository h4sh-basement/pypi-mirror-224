import sys
import pandas as pd
from starparser import argparser
from starparser import columnplay

"""
These functions still require explanations.
"""

"""
--limit
"""
def limitparticles(particles, column, limit, operator):
    
    tempcolumnname = column + "_float"
    particles[tempcolumnname] = particles[column]
    try:
        particles[tempcolumnname] = pd.to_numeric(particles[tempcolumnname], downcast="float")
    except ValueError:
        print("\n>> Error: this column doesn't seem to contain numbers.\n")
        sys.exit()
    limitedparticles = particles.copy()

    if operator == "lt":
        limitedparticles = limitedparticles[limitedparticles[tempcolumnname]<limit]
    elif operator == "gt":
        limitedparticles = limitedparticles[limitedparticles[tempcolumnname]>limit]
    elif operator == "ge":
        limitedparticles = limitedparticles[limitedparticles[tempcolumnname]>=limit]
    elif operator == "le":
        limitedparticles = limitedparticles[limitedparticles[tempcolumnname]<=limit]

    particles.drop(tempcolumnname,1, inplace=True)
    limitedparticles.drop(tempcolumnname,1, inplace=True)

    if len(limitedparticles.index) == 0:
        print("\n>> Error: there are no particles that match the criterion.\n")
        sys.exit()
    
    return(limitedparticles)

"""
--remove_particles
"""
def delparticles(particles, columns, query, queryexact):
    
    purgedparticles = particles.copy()
    
    if len(columns)>1:
        print("\n>> Error: you have specified two columns. You can't if you're querying to delete.\n")
        sys.exit()

    itisnumeric = True
    try:
        pd.to_numeric(particles[columns[0]], downcast="float")
    except ValueError:
        itisnumeric = False

    if not queryexact and itisnumeric:
        print("\n----------------------------------------------------------------------")        
        print("\n>> Warning: it looks like this column has numbers but you haven't specified the exact option (--e).\n   Make sure that this is the behavior you intended.\n")
        print("----------------------------------------------------------------------")

    if not queryexact:
        q = "|".join(query)
        purgedparticles.drop(purgedparticles[purgedparticles[columns[0]].str.contains(q)].index , 0,inplace=True)
    else:
        for q in query:
            purgedparticles.drop(purgedparticles[purgedparticles[columns[0]]==q].index , 0,inplace=True)
    
    return(purgedparticles)

"""
--remove_duplicates
"""
def delduplicates(particles, column):

    return(particles.drop_duplicates(subset=[column]))

"""
--remove_mics_fromlist
"""
def delmics(particles, micstodelete):
    purgedparticles = particles.copy()
    m = "|".join(micstodelete)
    purgedparticles.drop(purgedparticles[purgedparticles["_rlnMicrographName"].str.contains(m)].index , 0,inplace=True)    
    return(purgedparticles)

"""
--extract
"""
def extractparticles(particles, columns, query, queryexact):
    
    if len(columns)>1:
        print("\n>> Error: you have specified two columns. Only specify one if you're extracting from a subset of the data using a query.\n")
        sys.exit()

    itisnumeric = True
    try:
        pd.to_numeric(particles[columns[0]], downcast="float")
    except ValueError:
        itisnumeric = False

    params = argparser.argparse()

    if not queryexact and itisnumeric and not params["parser_splitoptics"] and not params["parser_classproportion"]:
        print("\n----------------------------------------------------------------------")        
        print("\n>> Warning: it looks like this column has numbers but you haven't specified the exact option (--e).\n   Make sure that this is the behavior you intended.\n")
        print("----------------------------------------------------------------------")

    if not queryexact:
        extractedparticles = particles.copy()
        q = "|".join(query)
        extractedparticles.drop(extractedparticles[~extractedparticles[columns[0]].str.contains(q)].index, 0,inplace=True)
    else:
        toconcat = [particles[particles[columns[0]] == q] for q in query]
        extractedparticles = pd.concat(toconcat)

    extractednumber = len(extractedparticles.index)
    
    return(extractedparticles, extractednumber)

def checksubset(particles, queryexact):
    
    """
    Re-processing the columns/queries is inefficient since it was
    already processed in decision tree. This also makes it so that
    you can't use checksubset in scripts. Consider revising.
    """

    params = argparser.argparse()
    if params["parser_column"] != "" and params["parser_query"] != "":

        query = params["parser_query"]
        escape = ",/"
        query = str.replace(params["parser_query"],escape, ",")
        query = query.split("/")
        for i,q in enumerate(query):
            query[i] = str.replace(q,",", "/")

        columns = params["parser_column"].split("/")
        
        subsetparticles, extractednumber = extractparticles(particles, columns, query, queryexact)
        
        print("\n>> Created a subset of " + str(extractednumber) + " particles (out of " + str(len(particles.index)) + ", " + str(round(extractednumber*100/len(particles.index),1)) + "%) that match " + str(query) +               " in the columns " + str(columns) + ".")
        
        return(subsetparticles)
    
    else:
        return(particles)

def countqueryparticles(particles,columns,query,queryexact,quiet):

    totalparticles = len(particles.index)
    
    totalquery = 0
    
    if len(columns)>1:
        print("\n>> Error: you have specified two different columns.\n")
        sys.exit()

    itisnumeric = True
    try:
        pd.to_numeric(particles[columns[0]], downcast="float")
    except ValueError:
        itisnumeric = False

    if not queryexact and itisnumeric:
        print("\n----------------------------------------------------------------------")        
        print("\n>> Warning: it looks like this column has numbers but you haven't specified the \"exact\" option (--e, see documentation).\n   Make sure that this is the behavior you intended.\n")
        print("----------------------------------------------------------------------")

    if not queryexact:
        q = "|".join(query)
        totalquery += len(particles[particles[columns[0]].str.contains(q)].index)
    else:
        for q in query:
            totalquery += len(particles[particles[columns[0]]==q].index)
        
    percentparticles = round(totalquery*100/totalparticles,1)

    if not quiet:
        print('\n>> There are ' + str(totalquery) + ' particles that match ' + str(query) + ' in the specified columns (out of ' + str(totalparticles) + ', or ' + str(percentparticles) + '%).\n')

    return(totalquery)

"""
--regroup
"""
def regroup(particles, numpergroup):
    
    newgroups = []
    roundtotal = int(len(particles.index)/numpergroup)
    leftover = (len(particles.index)) - roundtotal*numpergroup
    for i in range(roundtotal):
        newgroups.append([i+1 for j in range(numpergroup)])
    newgroups.append([newgroups[-1][-1] for i in range(leftover)])
    newgroups = [item for sublist in newgroups for item in sublist]

    regroupedparticles = particles.copy()
    regroupedparticles.sort_values("_rlnDefocusU", inplace=True)

    if "_rlnGroupNumber" in regroupedparticles.columns:
        regroupedparticles.drop("_rlnGroupNumber", 1, inplace=True)
        regroupedparticles["_rlnGroupNumber"] = newgroups

    if "_rlnGroupName" in regroupedparticles.columns:
        regroupedparticles.drop("_rlnGroupName", 1, inplace=True)
        newgroups = [("group_"+str(i).zfill(4)) for i in newgroups]
        regroupedparticles["_rlnGroupName"] = newgroups
    
    regroupedparticles.sort_index(inplace = True)
    regroupedparticles = regroupedparticles[particles.columns]

    return(regroupedparticles, roundtotal)

"""
--new_optics (also see setparticeoptics())
"""
def makeopticsgroup(particles,metadata,newgroup):
    
    optics = metadata[2]
    
    newoptics = optics.append(optics.loc[len(optics.index)-1], ignore_index = True)
    
    newoptics.loc[len(newoptics.index)-1]["_rlnOpticsGroupName"] = newgroup
    
    opticsnumber = int(newoptics.loc[len(newoptics.index)-1]["_rlnOpticsGroup"]) + 1
    
    newoptics.loc[len(newoptics.index)-1]["_rlnOpticsGroup"] = opticsnumber
    
    return(newoptics, opticsnumber)

"""
--new_optics (also see makeopticsgroup())
"""
def setparticleoptics(particles,column,query,queryexact,opticsnumber):
    
    particlesnewoptics = particles.copy()

    numchanged = countqueryparticles(particles, column, query, queryexact, True)
    
    if not queryexact:
        q = "|".join(query)
        particlesnewoptics.loc[particles[column[0]].str.contains(q), "_rlnOpticsGroup"] = opticsnumber
    else:
        for q in query:
            particlesnewoptics.loc[particles[column[0]]==q, "_rlnOpticsGroup"] = opticsnumber
        
    return(particlesnewoptics, numchanged)

"""
--import_particle_values
"""
def importpartvalues(original_particles, importfrom_particles, columnstoswap):

    importedparticles = original_particles.copy()

    for index, particle in original_particles.iterrows():
        imagename = particle["_rlnImageName"]
        importloc = importfrom_particles.index[importfrom_particles["_rlnImageName"] == imagename].tolist()
        if len(importloc) > 1:
            print("\n>> Error: " + imagename + " exists more than once in the star file.\n")
            sys.exit()
        importloc = importloc[0]
        for c in columnstoswap:
            importedparticles[c].iloc[index] = importfrom_particles[c].iloc[importloc]

    return(importedparticles)

"""
--expand_optics
"""

def expandoptics(original_particles, original_metadata, newdata, newdata_metadata, opticsgrouptoexpand):

    #print(original_metadata)
    #print(original_particles["_rlnMicrographName"])
    #print(original_particles["_rlnOpticsGroup"].head())

    if "_rlnMicrographName" not in original_particles.columns:
        print("\n>> Error: the star file doesn't have a _rlnMicrographName column.\n")
        sys.exit()
    elif "_rlnMicrographName" not in newdata.columns:
        print("\n>> Error: the second star file doesn't have a _rlnMicrographName column.\n")
        sys.exit()

    newmetadata = original_metadata

    opticsgroupnum = int(original_metadata[2].loc[original_metadata[2]["_rlnOpticsGroupName"] == opticsgrouptoexpand]["_rlnOpticsGroup"].tolist()[0])
    opticsgrouplist = original_metadata[2]["_rlnOpticsGroup"].tolist()
    opticsgrouplist = [int(o) for o in opticsgrouplist]

    importopticsnames = newdata_metadata[2]["_rlnOpticsGroupName"].tolist()
    importopticsnums = newdata_metadata[2]["_rlnOpticsGroup"].tolist()
    importopticsnums = [int(o) for o in importopticsnums]
    totalimportoptics = len(importopticsnums)

    #print(opticsgroupnum,opticsgrouplist,importopticsnums,totalimportoptics)

    newoptics = original_metadata[2]
    #print(newoptics["_rlnOpticsGroup"])

    torepeat = []
    for i,o in enumerate(opticsgrouplist):
        i=i+1
        if i < opticsgroupnum:
            torepeat.append(1)
            #continue
        elif i == opticsgroupnum:
            torepeat.append(totalimportoptics)
        else:
            torepeat.append(1)

        #opticsgrouplist[i]+=totalimportoptics

    #print(torepeat)
    newoptics["times"] = torepeat

    newoptics=newoptics.loc[newoptics.index.repeat(newoptics.times)].reset_index(drop=True)

    newoptics["_rlnOpticsGroup"] = range(1,totalimportoptics+len(opticsgrouplist))
    newoptics.drop("times",1, inplace=True)

    newopticsnames = newoptics["_rlnOpticsGroupName"].tolist()

    #print(newoptics)

    j=0
    for i,o in enumerate(newopticsnames):
        if o == opticsgrouptoexpand:
            newopticsnames[i] = importopticsnames[j]
            j+=1

    newoptics["_rlnOpticsGroupName"]=newopticsnames

    newmetadata[2] = newoptics

    #print(newoptics)

    #original_particles["_rlnOpticsGroup"] = pd.to_numeric(original_particles["_rlnOpticsGroup"], downcast="integer")

    particleoptics = original_particles["_rlnOpticsGroup"].tolist()
    newparticleoptics = [int(p) for p in particleoptics]

    for i,p in enumerate(newparticleoptics):
        if p <= opticsgroupnum:
            continue
        else:
            newparticleoptics[i]=str(int(p+totalimportoptics-1))

    original_particles["_rlnOpticsGroup"] = newparticleoptics

    ###############

    #print(newdata)

    newdataoptics = newdata["_rlnOpticsGroup"].tolist()
    newdataoptics = [int(p) for p in newdataoptics]

    for i,p in enumerate(newdataoptics):
        newdataoptics[i]=str(int(p+opticsgroupnum-1))

    newdata["_rlnOpticsGroup"] = newdataoptics

    #print(newdata)

    ####

    #print(original_particles["_rlnOpticsGroup"].head())

    expandedparticles = columnplay.importmicvalues(original_particles, newdata, "_rlnOpticsGroup")

    totaldifferent = 0
    for i, j in zip(original_particles.iterrows(), expandedparticles.iterrows()):
        if i[1]["_rlnOpticsGroup"] != j[1]["_rlnOpticsGroup"]:
            totaldifferent += 1

    print("\n>> The number of particles that have acquired a new optics group number = " + str(totaldifferent) + "\n")

    return(expandedparticles, newmetadata)
