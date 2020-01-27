### MYSQL의 정규표현식

| Symbol | Description                                         | Example                                                      |
| :----- | :-------------------------------------------------- | :----------------------------------------------------------- |
| *      | Represents zero or more characters                  | bl* finds bl, black, blue, and blob                          |
| ?      | Represents a single character                       | h?t finds hot, hat, and hit                                  |
| []     | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit                        |
| !      | Represents any character not in the brackets        | h[!oa]t finds hit, but not hot and hat                       |
| -      | Represents a range of characters                    | c[a-b]t finds cat and cbt                                    |
| #      | Represents any single numeric character             | 2#5 finds 205, 215, 225, 235, 245, 255, 265, 275, 285, and 295 |





### Wildcard Characters in SQL Server

| Symbol | Description                                         | Example                                |
| :----- | :-------------------------------------------------- | :------------------------------------- |
| %      | Represents zero or more characters                  | bl% finds bl, black, blue, and blob    |
| _      | Represents a single character                       | h_t finds hot, hat, and hit            |
| []     | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit  |
| ^      | Represents any character not in the brackets        | h[^oa]t finds hit, but not hot and hat |
| -      | Represents a range of characters                    | c[a-b]t finds cat and cbt              |





| LIKE Operator                   | Description                                                  |
| :------------------------------ | :----------------------------------------------------------- |
| WHERE CustomerName LIKE 'a%'    | Finds any values that starts with "a"                        |
| WHERE CustomerName LIKE '%a'    | Finds any values that ends with "a"                          |
| WHERE CustomerName LIKE '%or%'  | Finds any values that have "or" in any position              |
| WHERE CustomerName LIKE '_r%'   | Finds any values that have "r" in the second position        |
| WHERE CustomerName LIKE 'a_%_%' | Finds any values that starts with "a" and are at least 3 characters in length |
| WHERE ContactName LIKE 'a%o'    | Finds any values that starts with "a" and ends with "o"      |