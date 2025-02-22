using Eirene
using DelimitedFiles
using PlotlyJS

function persistent_homology(csv_data, dim)
    """
    function that computes persistent homology with the Vietoris–Rips filtration
    through pointcloud data and ouputs results.
    
    """
    point_cloud = readdlm(csv_data, ',')
    return eirene(point_cloud, maxdim=dim, model="pc")
end

function feature_extraction(PH_data)
    """
    Extracts data from PH such as persistence lifetimes.
    Data : barcode, persistence Landscape.
    """
    b = barcode(PH_data, dim=0)
    N = size(PH_data, 1)
    P_lifetimes = [b[i, 2] - b[i, 1] for i in 1:N if isfinite(b[i, 2])]
    writedlm("barcode", P_lifetimes, ',')
end


PH_data = persistent_homology("sphere_coordinates.csv", 1)
feature_extraction(PH_data)