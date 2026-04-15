<h2><a href="https://leetcode.com/problems/power-of-two">Power of Two</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

<hr>

<p><strong>Solution:</strong></p>

Two implementations. The first implementaiton constantly divide the number by 2, if you reach 1, then return True. If you reach any number not evenly divisible by 2, then it is False. Complexity: O(logn)

The second implementation, just check the binary of the number with an _and_ operation with the previous number. If it is zero then it is True, otherwise False. 
The binary representation of any number power of 2 is 1 followed by zeros. Then an _and_ operation would be all zeros. 
Example: 2^3 -> 8 -> 1000, _and_ 7 -> 0011 is 000. 
The counter example: 6 -> 0110 _and_ 5 -> 0101 is 0100, which is not zero. 
Complexity: O(1)
