var md = require('markdown-it')({
  html: true,
  linkify: true,
  typography: true
}).use(require('markdown-it-video'),
{
  youtube: { width: 640, height: 390 },
  vimeo: { width: 500, height: 281 },
  vine: { width: 600, height: 600, embed: 'simple' },
  prezi: { width: 550, height: 400 }
})
# Depth First Search
* *Depth First Search* is a graph traversal algorithm which explores as far as possible along each branch before backtracking
* Time Complexity: `O(|V| + |E|)`

![Alt text](../images/dfs.gif?raw=true "DFS Traversal")

@[youtube](o8S2bO3pmO4&)
