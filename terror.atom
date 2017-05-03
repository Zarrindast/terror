setwd("whatever")
library("igraph")

edges=read.csv("edges.csv")

g=graph.data.frame(edges,directed=FALSE)

E(g)$weight <- 1

g <- g - vertex("Unknown")
g <- g - vertex("Other")
g <- g - vertex("Individual")
g <- g - vertex("Gunmen")
# we dont want two groups who collaborated with unknown individuals to be
# considered one degree of separation on that basis XD

g <- simplify(g, remove.multiple = TRUE, remove.loops = TRUE,
  edge.attr.comb="sum")
# turns the multiplicity of the edges into a weight attribute

V(g)$realname <- V(g)$name
V(g)$index <- as.numeric(V(g))



clu <- components(g)
# membership is
#no is number of components
#csize is size of cluster

decomp_vxs_g <- groups(clu)
#shows the actual clusters in terms of vertices
#now decomp_vxs[[*]] gives you the *th cluster

decomp_edges_g <- decompose.graph(g)
#shows the clusters in terms of edges
#now decomp_edges[[*]] gives you the *th cluster

small.clusters <- which(clu$csize <= 2)
which(clu$membership %in% small.clusters)

largest <- which.max(sapply(decomp_edges_g, vcount))


eig <- eigen_centrality(g, directed = FALSE, scale = TRUE, weights = NULL,
  options = arpack_defaults)

sort(eig$vector, decreasing=TRUE)
#list by connectedness

which.max(eig$vector)
# the most network-influential terrorist group in the world! behold!

largest_cliques(g)
#arguments: min, max, subset, file

#fastgreedy network
fg <- fastgreedy.community(g)
colors <- rainbow(max(membership(fg)))
V(g)$label.cex <- .3
V(g)$name <- V(g)$index
V(g)[realname=="Al-Qaeda"]$name <- "AQ"
V(g)[realname=="Al-Qaeda"]$label.cex <- .5
V(g)[realname=="Al-Qaeda"]$label.color <- "white"
V(g)[realname=="Hamas"]$name <- "H"
V(g)[realname=="Hamas"]$label.cex <- .7
V(g)[realname=="Hamas"]$label.color <- "white"
V(g)[realname=="Taliban"]$name <- "T"
V(g)[realname=="Taliban"]$label.cex <- .7
V(g)[realname=="Taliban"]$label.color <- "white"
V(g)[realname=="Boko Haram"]$name <- "BH"
V(g)[realname=="Boko Haram"]$label.cex <- .5
V(g)[realname=="Boko Haram"]$label.color <- "white"
V(g)[realname=="Islamic State of Iraq and the Levant (ISIL)"]$name <- "IS"
V(g)[realname=="Islamic State of Iraq and the Levant (ISIL)"]$label.cex <-.5
V(g)[realname=="Islamic State of Iraq and the Levant (ISIL)"]$label.color <- "white"
plot(g,vertex.color=colors[membership(fg)], layout=layout.fruchterman.reingold,
vertex.size=5)
