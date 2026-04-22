<h2><a href="https://leetcode.com/problems/convert-a-number-to-hexadecimal">Convert a Number to Hexadecimal</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a 32-bit integer <code>num</code>, return <em>a string representing its hexadecimal representation</em>. For negative integers, <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">two&rsquo;s complement</a> method is used.</p>

<p>All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.</p>

<p><strong>Note:&nbsp;</strong>You are not allowed to use any built-in library method to directly solve this problem.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 26
<strong>Output:</strong> "1a"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = -1
<strong>Output:</strong> "ffffffff"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<hr>

Solution:

I created a map for hexadcimals like the following: {10: "a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}. Then I convert from base 10 to base 16 by dividing by 16 and attaching the rest, then apply the mapping for the rest. If the number is negative the representation is inverted, so I sum the negative number to the max representation there is 2^32. Complexity: O(logn)
