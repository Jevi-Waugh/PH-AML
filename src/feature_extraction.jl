using Eirene
using DelimitedFiles
using PlotlyJS
using Statistics

function persistent_homology(csv_data, dim)
    """
    function that computes persistent homology with the Vietoris–Rips filtration
    through pointcloud data and ouputs results.
    
    """
    point_cloud = readdlm(csv_data, ',')
    return eirene(point_cloud, maxdim=dim, model="pc")
end

function feature_extraction(PH_data, num)
    """
    Extracts data from PH such as persistence lifetimes.
    Data : barcode, persistence Landscape.
    """
    b = barcode(PH_data, dim=0)
    N = size(b, 1)
    P_lifetimes = [b[i, 2] - b[i, 1] for i in 1:N if isfinite(b[i, 2])]
    writedlm("persistence_diagram_$(num).csv", b, ',')
    writedlm("topological_descriptors_$(num).csv", P_lifetimes, ',')
    return P_lifetimes
end

function persistent_statistics(lifetimes,num)
    # Compute persistence statistics
    mean_lifetime = mean(lifetimes)      # Mean lifetime
    std_lifetime = std(lifetimes)        # Standard deviation
    max_lifetime = maximum(lifetimes)    # Longest-lived feature
    sum_lifetime = sum(lifetimes)        # Total persistence sum

    # Store as a feature vector
    stat_features = [mean_lifetime, std_lifetime, max_lifetime, sum_lifetime]

    # Save to CSV for ML training
    writedlm("persistence_statistics_$(num).csv", permutedims(stat_features), ',')
end


PH = persistent_homology("torus_coordinates_0.csv", 1)
lifetimes = feature_extraction(PH,1)
persistent_statistics(lifetimes,1)
