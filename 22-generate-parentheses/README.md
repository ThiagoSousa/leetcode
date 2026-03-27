<h2><a href="https://leetcode.com/problems/generate-parentheses">Generate Parentheses</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>

<hr>

<p><strong>Solutions:</strong></p>

Depth first search that opens parenthesis if the number of open parenthis is smaller than n, and closes if the number of closed parenthesis is smaller than the number of opens. 

Complexity-wise, tt doesn't explore all the 2^2n possibilities, as it prunes invalid prefixes. So the number of outputs are given to Catalan number, thus the complexity is O(cn*n)
