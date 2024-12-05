pageOrderingRulesMap = {}
middlePageSum = 0

with open('input/day5.txt', 'r') as f:
    isInPageOrderingRulesSection = True
    for line in f:
        if isInPageOrderingRulesSection:
            if line == '\n':
                isInPageOrderingRulesSection = False
            else:
                pages = line.split('|')
                pagesThatMustComeAfter = pageOrderingRulesMap.get(int(pages[0]), [])
                pagesThatMustComeAfter.append(int(pages[1]))
                pageOrderingRulesMap[int(pages[0])] = pagesThatMustComeAfter
        else:
            pageOrderIndexMap = {}

            pages = line.split(',')
            for i in range(len(pages)):
                pageOrderIndexMap[int(pages[i])] = i 

            validOrder = True
            for page in pageOrderIndexMap.keys():
                for futurePage in pageOrderingRulesMap.get(page, []):
                    if pageOrderIndexMap.get(futurePage, float('inf')) < pageOrderIndexMap[page]:
                        validOrder = False
                        break
                if not validOrder:
                    break
            if validOrder:
                middlePageSum += int(pages[len(pages) // 2])

print('PART 1: %d' % middlePageSum)

