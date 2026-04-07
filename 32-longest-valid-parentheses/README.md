<h2><a href="https://leetcode.com/problems/longest-valid-parentheses">Longest Valid Parentheses</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, return <em>the length of the longest valid (well-formed) parentheses </em><span data-keyword="substring-nonempty"><em>substring</em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>

<hr>

Implementation uses a queue to store the positions of opening and closing parethesis. If it finds a new opening parenthesis it inserts in the queue. For closing parethesis, it checks if there is a matching opening parenthesis in the last position of the queue, if so dequeue it. Otherwise inserts in the queue. After passing through the string, the queue will only contain positions with wrong parethesis, then I simply the difference between these positions and save the biggest which is the max_length. Complexity: O(n*m) where n is the size of the list and m is the number of wrong elements in the list. O(n^2) in the worst scenario, if all of the elements are wrong. I added a condition, if the queue is empty, then the result is immediately the list of O(n).
 
