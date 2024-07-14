#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

struct Point {
	double x, y, z;
	int r, g, b;
};

bool isInsideBox(const Point& point, double boxSize, double startX, double startY){

	//std::cout << "Inside" <<std::endl;
	double endX = startX + boxSize / 2.0;
	double endY = startY + boxSize / 2.0;
	//double endZ = startZ + boxSize / 2.0;

	double beginX = startX - boxSize / 2.0;
	double beginY = startY - boxSize / 2.0;
	//double beginZ = startZ - boxSize / 2.0;

	return (point.x >= beginX && point.x <= endX &&
		point.y >= beginY && point.y <= endY);

//	return (point.x >= beginX && point.x <= endX &&
//		point.y >= beginY && point.y <= endY &&
//		point.z >= beginZ && point.z <= endZ);
}

int main(){
	// Open input and output files
	std::ifstream inputFile("filtered.ply");
	std::ofstream outputFile("final.ply");

	// Check if files are opened successfully
	if (!inputFile.is_open() || !outputFile.is_open()) {
		std::cerr << "error opening files!" << std::endl;
		return 1;
	}

	// Vector to hold points read from the input file
	std::vector<Point> points;
	std::string line;
	// Vector to hold header lines
	std::vector<std::string> headerLines;

	// Read and store header lines
	for (int i = 0; i < 10; i++){
		std::getline(inputFile, line);
		headerLines.push_back(line);
	}

	// Read each line from input file
	while (std::getline(inputFile, line)) {
		std::istringstream iss(line);
		Point point;
		// Parse the line into point coordinates and RGB values
		if (!(iss >> point.x >> point.y >> point.z >> point.r >> point.g>> point.b)) {
			std::cerr << "Error reading input file!" << std::endl;
			return 1;
		}
		// Add the parsed point to the vector
		points.push_back(point);
	}

	// Define the size of the box
	double boxSize = 0.01875;
	double startX  = -0.5;
	double startY  = -0.25;
	//double startZ  = 0.85;


	// Write header lines to the output file
	for (const auto& headerLine : headerLines) {
		outputFile << headerLine << std::endl;
	}


	// Itterate through all points
	for (const auto& point : points) {

		Point temp_point;
		if (isInsideBox(point, boxSize, startX, startY)) {
			// If yes, change the color to red and add it to filteredPoints
			outputFile << point.x << " " << point.y << " " << point.z << " " 
				<< 255 << " " << 0 << " " << 0 << std::endl;

		} else {
			// If yes, change the color to red and add it to filteredPoints
			outputFile << point.x << " " << point.y << " " << point.z << " " 
				<< point.r << " " << point.g << " " << point.b << std::endl;

		}
	}

	// Close input and output files 
	inputFile.close();
	outputFile.close();

	// Inform user about successful completion
	std::cout << "Filtered points saved to 'final.ply'." << std::endl;

	return 0;

}
