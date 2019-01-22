fileResult = open("toDo1/result.txt", "w")

# Create the agents and the variables sections

allAgents = ""
nbAgents = 0
allVariables = ""

# Read the var
with open("toDo1/var.txt", "r") as file:
    for line in file:
        elt = line.split(' ')
        elt = list(filter(None, elt))
        elt[-1] = elt[-1].split('\n')[0]
        allAgents += '\t\t<agent name="agent' + elt[0] + '" />\n'
        nbAgents += 1
        allVariables += '\t\t<variable name="' + elt[0] + '" domain="domain' + elt[1] + '" agent="agent' + elt[
            0] + '"/>\n'

allAgents = '\t<agents nbAgents="' + str(nbAgents) + '">\n' + allAgents + '\t</agents>\n\n'
allVariables = '\t<variables nbVariables="' + str(nbAgents) + '">\n' + allVariables + '\t</variables>\n\n'

# Create the domains section

allDomains = ""
nbDomains = 0

# Read the dom
with open("toDo1/dom.txt", "r") as file:
    for line in file:
        elt = line.split(' ')
        elt = list(filter(None, elt))
        elt[-1] = elt[-1].split('\n')[0]
        domain = ' '.join(elt[2:])

        allDomains += '\t\t<domain name="domain' + str(elt[0]) + '" nbValues="' + str(
            elt[1]) + '">' + domain + '</domain>\n'
        nbDomains += 1

allDomains = '\t<domains nbDomains="' + str(nbDomains) + '">\n' + allDomains + '\t</domains>\n\n'

# Create the constraints section

allConstraints = ""
nbConstraints = 0

# Read the ctr
with open("toDo1/ctr.txt", "r") as file:
    for line in file:
        elt = line.split(' ')
        elt = list(filter(None, elt))
        elt[-1] = elt[-1].split('\n')[0]

        relation = ""
        if elt[3] == "=":
            relation = "equal"
        else:
            relation = "greaterThan"

        allConstraints += '\t<constraint name="' + elt[0] + '_' + elt[1] + '_relation_' + elt[
            2] + '" arity="2" scope="' + elt[0] + ' ' + elt[
                              1] + '" reference="' + relation + '" >\n\t\t' + '<parameters> ' + elt[0] + ' ' + elt[
                              1] + ' ' + elt[-1] + ' </parameters>\n' + '\t</constraint>\n'
        nbConstraints += 1

allConstraints = '\t<constraints nbConstraints="' + str(nbConstraints) + ' ">\n' + allConstraints + '\t</constraints>\n\n'

# Create the predicates section

allPredicates = '\t<predicates nbPredicates="2">\n' \
                '\t\t<predicate name="greaterThan">\n' \
                '\t\t\t<parameters> int X1 int X2 int d </parameters>\n' \
                '\t\t\t<expression>\n' \
                '\t\t\t\t<functional> if(ge(abs(sub(X1, X2)), d), abs(X1, X2), infinity) </functional>\n' \
                '\t\t\t</expression>\n' \
                '\t\t</predicate>\n' \
                '\t\t<predicate name="equal">\n' \
                '\t\t\t<parameters> int X1 int X2 int d </parameters>\n' \
                '\t\t\t<expression>\n' \
                '\t\t\t\t<functional> if(eq(abs(sub(X1, X2)), d), 0, infinity) </functional>\n' \
                '\t\t\t</expression>\n' \
                '\t</predicates>\n\n'

print(allPredicates)

# Write the header
fileResult.write(
    '<instance>\n'
    '<presentation name="masPRELIMINARY" maxConstraintArity="2" maximize="false" format="XCSP 2.1_FRODO"/> \n\n')

# Write all the sections
fileResult.write(allAgents)
fileResult.write(allDomains)
fileResult.write(allVariables)
fileResult.write(allPredicates)
fileResult.write(allConstraints)

# Write the tail
fileResult.write('</instance>')

fileResult.close()
