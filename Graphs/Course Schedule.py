"""
QUESTION (Problem 207)

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

- Example 1
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

- Example 2
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

PROBLEM EXPLANATION AND TEST CASE VALIDATION

This question essentially boils down to detecting a cycle in a graph. 
We are only able to finish all courses if there are no cycles in the course mapping.

- In Example 1:
Our prerequisites mapping can be represented in this graph format:

1 -> 0

As you can see there are no cycles in this graph therefore we can finish all the courses so we return True. 

- In Example 2
Our prerequisites mapping can be represented in this graph format:

1->0
^ /
|/   

As you can see we have a cycle in this graph therefore we cannot finish all the courses due to inter dependency so we return False. 


SOLUTION APPROACH

We can detect a cycle in a graph through a topological sort of the graph. This means traversing the graph by making the courses that do not
have any prerequisites our main priority. If we are able to visit every node then there are no cycles, if not then a cycle exists.

Steps

1. Create a mapping in an array where each index is a course and the value is the number of prerequisites for that course i.e inDegree.
2. Traverse the graph using a stack starting with courses that are devoid of any prerequisites. i.e inDegree[course] ==0.
3. For each course we process it by incrementing a visited counter and also reducing the number of prerequisites of any other course having our current course as a prerequisite.
4. The next course to go into the stack will be a course without any prerequisites.
5. At the end we check to see if the number of visited courses equals the total number of courses.

Time Complexity is O(n) becuase we would visit every node at least once.
Space Complexity is also O(n) because we are making use of two extra arrays (a stack and 'inDegree') both having a maximum size of n.
"""

# Solution

def canFinish(numCourses, prerequisites):
    
    inDegree = [0] * numCourses
    stack = []
    visited = 0
    
    for course, pre in prerequisites:
        inDegree[course] +=1
        
    for i in range(numCourses):
        if inDegree[i] == 0:
            stack.append(i)
    
    while stack:
        
        curr_node = stack.pop()
        
        for course, pre in prerequisites:
            if pre == curr_node:
                inDegree[course] -=1
                if inDegree[course] == 0:
                    stack.append(course)
        visited+=1
                
    return visited == numCourses
         
            