#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

struct Point {
	double x, y, z;
	int r, g, b;
};

bool isInsideBox(const Point& point, double boxSize){
	return (fabs(point.x) <= boxSize / 2.0 &&
		fabs(point.y) <= boxSize / 2.0 &&
		fabs(point.z) <= boxSize / 2.0);
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
	double boxSize = 0.6;

	// Vector to hold filtered points
	std::vector<Point> filteredPoints;
	
	// Itterate through all points
	for (const auto& point : points) {
		if (isInsideBox(point, boxSize)) {
			// If yes, add to the filtered points vector
			filteredPoints.push_back(point);
		}
	}

	// Change the Total Vertex Lines number in the header in the second line
	if (headerLines.size() >= 3){
		// Extracting the second line from the headerLines vector
		std::string secondline = headerLines[2];
		// Using stringstream to extract values from the second line
		std::istringstream secondLineStream(secondline);
		
		std::string value1, value2, value3;

		if (secondLineStream >> value1 >> value2 >> value3){
			std::cout << "Second value of the second line in the header: " << value3 << std::endl;
			std::cout << "Size of filtredPoints: " << filteredPoints.size() << std::endl;
			

			value3 = std::to_string(filteredPoints.size());
			headerLines[2] = value1 + " " + value2 + " " + value3;
		}

	}

	// Write header lines to the output file
	for (const auto& headerLine : headerLines) {
		outputFile << headerLine << std::endl;
	}

	// Write filtered points to the output file
	for (const auto& point : filteredPoints) {
		outputFile << point.x << " " << point.y << " " << point.z << " " 
			<< point.r << " " << point.g << " " << point.b << std::endl;  
	}

	// Close input and output files 
	inputFile.close();
	outputFile.close();

	// Inform user about successful completion
	std::cout << "Filtered points saved to 'final.ply'." << std::endl;

	return 0;

}
