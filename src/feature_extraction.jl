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
    Extracts data from PH.
    Data : barcode, persistence Landscape.
    """
    b = barcode(PH_data, dim=0)
    writedlm("barcode", b)
end


PH_data = persistent_homology("sphere_coordinates.csv", 1)
feature_extraction(PH_data)