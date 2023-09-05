#include <iostream>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <set>
#include <algorithm>

bool isSubsequence(const std::set<int> &set1, const std::set<int> &set2)
{
    auto it1 = set1.begin();
    auto it2 = set2.begin();

    while (it1 != set1.end() && it2 != set2.end())
    {
        if (*it1 == *it2)
        {
            ++it1;
        }
        ++it2;
    }

    return it1 == set1.end();
}

int main()
{
    int rows;
    std::cin >> rows;
    std::cin.ignore();
    std::vector<std::vector<int>> matrix;
    std::unordered_map<int, std::set<int>> intToSetMap;
    std::unordered_map<int, std::set<int>> arrSizeToIndicesMap;
    std::unordered_map<int, std::set<int>> childrens;
    std::vector<int> arrSizes;

    for (int i = 0; i < rows; ++i)
    {
        std::string inputLine;
        std::getline(std::cin, inputLine);
        std::vector<int> row;
        std::istringstream iss(inputLine);

        int num;
        std::set<int> setValues;
        int rowSize = 0;
        while (iss >> num)
        {
            row.push_back(num);
            setValues.insert(num);
            rowSize++;
        }
        arrSizes.push_back(rowSize);
        arrSizeToIndicesMap[rowSize].insert(i);
        intToSetMap[i] = setValues;
        matrix.push_back(row);
    }
    std::sort(std::begin(arrSizes), std::end(arrSizes));

    for (int i = 0; i < rows; i++)
    {
        std::set<int> visited;
        bool done = false;
        for (int j = 0; j < rows; j++)
        {
            if (arrSizes[j] > intToSetMap[i].size() and !done)
            {

                for (int index : arrSizeToIndicesMap[arrSizes[j]])
                {
                    if (isSubsequence(intToSetMap[i], intToSetMap[index]))
                    {
                        childrens[index].insert(i);
                        done = true;
                    }
                }
            }
        }
    }

    //
    for (int i = 0; i < rows; i++)
    {
        for (int child : childrens[i])
        {
            std::cout << child << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}