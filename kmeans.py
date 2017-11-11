#!/usr/bin/env python
"""
K-Means clustering intends to partition n objects into k clusters in which each object belongs
to the cluster with the nearest mean. This method produces exactly k different clusters of
greatest possible distinction.

The best number of clusters k leading to the greatest separation (distance) is not known as a priori and
must be computed from the data. The objective of K-Means clustering is to minimize total intra-cluster variance,
or, the squared error function.

Algorithm:
1. Clusters the data into k groups where k  is predefined.
2. Select k points at random as cluster centers.
3. Assign objects to their closest cluster center according to the Euclidean distance function.
4. Calculate the centroid or mean of all objects in each cluster.
5. Repeat steps 2, 3 and 4 until the same points are assigned to each cluster in consecutive rounds.

K-Means is relatively an efficient method. However, we need to specify the number of clusters, in advance and
the final results are sensitive to initialization and often terminates at a local optimum.
Unfortunately there is no global theoretical method to find the optimal number of clusters.
A practical approach is to compare the outcomes of multiple runs with different k
and choose the best one based on a predefined criterion.

In general, a large k probably decreases the error but increases the risk of overfitting.

Runtime: O(tnk)
t -> number of iterations
n -> number of data points
k -> number of clusters

More information: http://www.mit.edu/~9.54/fall14/slides/Class13.pdf
"""

import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cluster:
    """
    A collection of points and their centroid
    """
    def __init__(self, points):
        """
        :param points: A list of point objects
        """

        # The points that belong to this cluster
        self.points = points

        # Set up the initial centroid (this is usually based off one point)
        self.centroid = self.calculateCentroid()

    def calculateCentroid(self):
        """
        Finds a virtual center point for a group of Point objects
        """
        num_points = len(self.points)

        x_coords = [point.x for point in self.points]
        y_coords = [point.y for point in self.points]

        # Calculate the mean for each dimension
        centroid_x_mean = math.fsum(x_coords) / num_points
        centroid_y_mean = math.fsum(y_coords) / num_points

        return Point(centroid_x_mean, centroid_y_mean)

    def update(self, points):
        """
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.

        Note: Initially we expect centroids to shift around a lot and then
        gradually settle down.
        """
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid)
        return shift


# K-Means is an algorithm that takes in a dataset and a constant
# k and returns k centroids (which define clusters of data in the
# dataset which are similar to one another).

def kmeans(dataSet, k, cut_off, max_iterations):
    """
    :param dataSet:  A list of point objects
    :param k: Number of centroids to return
    :param cut_off: Shift in old and new centroids
    :param max_iterations: Max iterations to perform
    """
    if not dataSet:
        return []

    # Pick out k random points to use as our initial centroids
    initial = random.sample(dataSet, k)

    # Create k clusters using those centroids
    # Note: Cluster takes lists, so we wrap each point in a list here.
    clusters = [Cluster([point]) for point in initial]

    # Loop through the dataset until the clusters stabilize
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [[] for _ in clusters]
        clusterCount = len(clusters)

        for point in dataSet:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(point, clusters[0].centroid)

            # Set the cluster this point belongs to
            clusterIndex = 0

            # Now try to find a more appropriate cluster for this point
            for i in range(clusterCount - 1):
                distance = getDistance(point, clusters[i + 1].centroid)

                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i + 1

            # After finding the cluster that is closest to the current point,
            # set the point belongs to the cluster
            lists[clusterIndex].append(point)

        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0

        # For each cluster ...
        for i in range(len(clusters)):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])

            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)

        if biggest_shift < cut_off:
            print "Converged after %s iterations" % loopCounter
            break

        # check if we have crossed max iterations
        if loopCounter >= max_iterations:
            print "Converged after %s iterations" % loopCounter
            break

        # update loop counter
        loopCounter += 1

    return clusters


def getDistance(a, b):
    """
    Euclidean distance between two point objects
    """
    distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    return distance


def generate_random_points(n, lower, upper):

    points = []
    for _ in range(n):
        x_coord = random.uniform(lower, upper)
        y_coord = random.uniform(lower, upper)
        point = Point(x_coord, y_coord)
        points.append(point)

    return points


def main():

    # How many points are in our dataset?
    num_points = 20

    # Bounds for the values of those points in each dimension
    lower = 0
    upper = 100

    # The K in k-means. How many clusters do we assume exist?
    num_clusters = 3

    # When do we say the optimization has 'converged' and stop updating clusters
    cutoff = 0.2

    # Max iterations
    max_iterations = 500

    # Generate some points to cluster
    points = generate_random_points(num_points, lower, upper)

    # Cluster those data!
    clusters = kmeans(points, num_clusters, cutoff, max_iterations)

    # Print the cluster
    for idx, cluster in enumerate(clusters):
        for p in cluster.points:
            print " Cluster: ", idx, "\t Point X: ", p.x, "\t Point Y: ", p.y

if __name__ == '__main__':
    main()
