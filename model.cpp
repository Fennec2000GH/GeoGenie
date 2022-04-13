// C++ std libraries
#include <fstream>
#include <iostream>
#include <vector>

// C++ third party libraries
#include <Eigen/Dense>
// #include <dynet/dim.h>
// #include <dynet/dynet.h>
// #include "dynet/expr.h"
#include "dynet/model.h"
// #include "dynet/model.cc"
#include "dynet/tensor.h"
// #include "dynet/tensor.cc"
#include "dynet/training.h"
// #include "dynet/training.cc"
#include "dynet/treelstm.h"
// #include "dynet/treelstm.cc"

int main(int argc, char **argv) {
// 	// dynet::initialize(argc, argv);
// 	dynet::ParameterCollection pc(1.2);
// 	// dynet::SimpleSGDTrainer trainer(pc);


// 	// dynet::ComputationGraph cg;
// 	std::vector<dynet::real> input;
// 	// dynet::Expression w = parameter(cg, pc.add_parameters(dynet::Dim({12})));
// 	dynet::Tensor t;

// 	// cg.print_graphviz();

  dynet::NaryTreeLSTMBuilder builder;
  
	return 0;
}

