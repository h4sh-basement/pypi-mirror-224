#include "fiber_prop.h"
#include "simul_prop.h"
#include "python_utilities.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;
class Property;

/// a utility to enrich the cytosim python module
auto load_simul_classes(py::module_ &m) {
    /// Python interface to Vector
    auto pyVector = py::class_<Vector>(m, "Vector", py::buffer_protocol())
        .def_buffer([](Vector &vec) -> py::buffer_info {
            void * data = vec.data();
            //int_vect sizes =  {1, DIM};
            int_vect sizes =  {DIM};
            //int_vect strides =  {DIM*sizeof(real), sizeof(real)};
            int_vect strides =  {sizeof(real)};
            return py::buffer_info(
                   data,                               /* Pointer to buffer */
                   sizeof(real),                          /* Size of one scalar */
                   py::format_descriptor<real>::format(), /* Python struct-style format descriptor */
                   1,                                      /* Number of dimensions */
                   sizes,                 /* Buffer dimensions */
                   strides             /* Strides (in bytes) for each index */
                );
    });
    
#if (DIM !=3)    
    /// Python interface to Vector
    py::class_<Vector3>(m, "Vector3", py::buffer_protocol())
    .def_buffer([](Vector3 &vec) -> py::buffer_info {
        void * data = vec.data();
        int_vect sizes =  {3};
        int_vect strides =  {sizeof(real)};
        return py::buffer_info(
               data,                               /* Pointer to buffer */
               sizeof(real),                          /* Size of one scalar */
               py::format_descriptor<real>::format(), /* Python struct-style format descriptor */
               1,                                      /* Number of dimensions */
               sizes,                 /* Buffer dimensions */
               strides             /* Strides (in bytes) for each index */
               );
    });
#else
    m.attr("Vector3") = pyVector;
#endif
    
    /// Python interface to default property
    py::class_<Property>(m, "Prop")
        .def("name", &Property::name)
        .def("change", [](Property * prop, std::string winds, Simul * sim) {
            Glossary of_change = Glossary(winds);
            prop->read(of_change);
            prop->complete(*sim);
        })
        .def("read", [](Property * prop, std::string winds) {
            Glossary of_change = Glossary(winds);
            prop->read(of_change);
        })
        .def("change_glos", [](Property * prop, Glossary & winds, Simul * sim) {
            prop->read(winds);
            prop->complete(*sim);
        })
        .def("read_glos", [](Property * prop, Glossary & winds) {
            prop->read(winds);
        })
        .def("complete",  [](Property * prop, Simul * sim) {return prop->complete(*sim);})
        .def("rename", &Property::rename)
        .def("is_named", &Property::is_named)
        .def("number", &Property::number)
        .def("renumber", &Property::renumber)
        .def("clear", &Property::clear)
        .def("clone", &Property::clone, py::return_value_policy::reference);
        
        
    
    py::class_<SpaceSet,ObjectSet>(m, "SpaceSet");
	py::class_<FiberSet,ObjectSet>(m, "FiberSet");
	py::class_<FieldSet,ObjectSet>(m, "FieldSet");
	py::class_<SphereSet,ObjectSet>(m, "SphereSet");
	py::class_<BeadSet,ObjectSet>(m, "BeadSet");
	py::class_<SolidSet,ObjectSet>(m, "SolidSet");
	py::class_<OrganizerSet,ObjectSet>(m, "OrganizerSet");
	
    
    auto pysim = py::class_<Simul>(m, "Simul")
        .def("frame",  [](Simul * sim) {return Frame(sim);}, py::return_value_policy::move)
        .def_readwrite("prop",   &Simul::prop , py::return_value_policy::reference)
        .def_readwrite("sMeca",   &Simul::sMeca , py::return_value_policy::reference)
        .def_readwrite("properties",   &Simul::properties , py::return_value_policy::reference)
		.def_readonly("spaces",   &Simul::spaces , py::return_value_policy::reference)
        .def_readonly("fields",   &Simul::fields , py::return_value_policy::reference)
        .def_readonly("fibers",   &Simul::fibers , py::return_value_policy::reference)
        .def_readonly("spheres",   &Simul::spheres , py::return_value_policy::reference)
        .def_readonly("beads",   &Simul::beads , py::return_value_policy::reference)
        .def_readonly("solids",   &Simul::solids , py::return_value_policy::reference)
        .def_readonly("couples",   &Simul::couples , py::return_value_policy::reference)
        .def_readonly("singles",   &Simul::singles , py::return_value_policy::reference)
        .def_readonly("organizers",   &Simul::organizers , py::return_value_policy::reference)
        .def("remove",  [](Simul * sim, Object* obj) {return sim->remove(obj);})
        .def("erase",  [](Simul * sim, Object* obj) {return sim->erase(obj);})
        .def("nuke",  [](Simul * sim) {return sim->erase();})
        .def("time",  [](Simul * sim) {return sim->time();})
        .def("time_step",  [](Simul * sim) {return sim->time_step();})
        .def("step",  [](Simul * sim) {return sim->step();})
        .def("ready", &Simul::ready)
        .def("computeForces",  &Simul::computeForces)
        .def("once",  [](Simul * sim) { sim->solve() ; sim->step(); })
        .def("prepared_solve",  &Simul::prepared_solve)
        .def("prepare_meca",  &Simul::prepare_meca)
        .def("prepare",  [](Simul * sim) { sim->prepare();} )   
        .def("solve",  [](Simul * sim) {return sim->solve();})
        .def("solve_auto",  [](Simul * sim) {return sim->solve_auto();})
        //.def("dump",  [](Simul * sim, std::string s) {return sim->dump( &s[0]);})
        //.def("saveSystem",  [](Simul * sim, char s) {return sim->saveSystem((char) s);})
        .def("evaluate",  [](Simul * sim, std::string s) {return sim->evaluate(s);} , py::return_value_policy::reference)
        .def("toMecable",  [](Simul * sim, Object* o) {return sim->toMecable(o);} , py::return_value_policy::reference)
        .def("findMecable",  [](Simul * sim, std::string s) {return sim->findMecable(s);} , py::return_value_policy::reference)
        .def("findSpace",  [](Simul * sim, std::string s) {return sim->findSpace(s);} , py::return_value_policy::reference)
        .def("rename",  [](Simul * sim, std::string s) {return sim->rename(s);} , py::return_value_policy::reference)
        .def("isCategory",  [](Simul * sim, std::string s) {return sim->isCategory(s);} , py::return_value_policy::reference)
        .def("findProperty",  [](Simul * sim, std::string s) {return sim->findProperty(s);} , py::return_value_policy::reference)
        .def("writePropertiesTo",  [](Simul * sim, std::string s) {return sim->writeProperties(&s[0],1);} )
        .def("writeProperties",  [](Simul * sim, bool prune) {return sim->writeProperties(&sim->prop->property_file[0], prune);} )
        .def("writePropertiesToNoPrune",  [](Simul * sim, std::string  s) {return sim->writeProperties(&s[0],0);} );
        
        
    
    /// Python interface to simulProp
    py::class_<SimulProp,Property>(m, "SimulProp")
        .def_readwrite("time", &SimulProp::time)
        .def_readwrite("time_step", &SimulProp::time_step)
        .def_readwrite("viscosity", &SimulProp::viscosity)
        .def_readwrite("kT", &SimulProp::kT)
        .def_readwrite("tolerance", &SimulProp::tolerance)
        .def_readwrite("acceptable_prop", &SimulProp::acceptable_prob)
        .def_readwrite("precondition", &SimulProp::precondition)
        .def_readwrite("steric", &SimulProp::steric)
        .def("steric_stiffness_push",  [](SimulProp * prop) {return to_numpy_raw(prop->steric_stiffness_push, 1, 2); })
        .def("steric_stiffness_pull",  [](SimulProp * prop) {return to_numpy_raw(prop->steric_stiffness_pull, 1, 2); })
        .def_readwrite("steric_max_range", &SimulProp::steric_max_range)
        .def_readwrite("binding_grid_step", &SimulProp::binding_grid_step)
        .def_readwrite("verbose", &SimulProp::verbose)
        .def_readwrite("config_file", &SimulProp::config_file)
        .def_readwrite("property_file", &SimulProp::property_file)
        .def_readwrite("trajectory_file", &SimulProp::trajectory_file)
        .def_readwrite("clear_trajectory", &SimulProp::clear_trajectory)
        .def_readwrite("skip_free_couple", &SimulProp::skip_free_couple)
        .def_readwrite("display_fresh", &SimulProp::display_fresh)
        .def_readwrite("display", &SimulProp::display)
        .def("read",  [](SimulProp * prop, Glossary & glos) {return prop->read(glos);})
        .def("read_str",  [](SimulProp * prop, std::string const& str) {return prop->read(str_to_glos(str));})
        .def("clone",  [](SimulProp * prop) {return prop->clone();});
        

    return pysim;
}

