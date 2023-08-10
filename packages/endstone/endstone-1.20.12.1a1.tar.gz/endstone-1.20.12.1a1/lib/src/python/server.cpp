//
// Created by Vincent on 31/07/2023.
//

#include "python/server.h"

Server::Server() : logger_(Logger::getLogger("Server"))
{
    py::gil_scoped_acquire lock{};
    // https://github.com/pybind/pybind11/issues/2197
    py::module_::import("threading");
}

void Server::loadPlugins()
{
    py::gil_scoped_acquire lock{};
    pluginManager_.attr("load_plugins")((std::filesystem::current_path() / "plugins").string());
}

void Server::enablePlugins()
{
    py::gil_scoped_acquire lock{};
    pluginManager_.attr("enable_plugins")();
}

void Server::disablePlugins()
{
    py::gil_scoped_acquire lock{};
    pluginManager_.attr("disable_plugins")();
}

void Server::clearPlugins()
{
    py::gil_scoped_acquire lock{};
    pluginManager_.attr("clear_plugins")();
}

void Server::start()
{
    try
    {
        logger_.info("Endstone Version: %s", Endstone::getVersion().c_str());
        py::gil_scoped_acquire lock{};
        auto module = py::module_::import("endstone.plugin");
        auto cls = module.attr("PluginManager");
        pluginManager_ = cls(this);
    }
    catch (py::error_already_set &e)
    {
        logger_.error("Failed to load PluginManager with Python exceptions: %s\n", e.what());
        throw e;
    }
    catch (const std::exception &e)
    {
        logger_.error("Failed to load PluginManager with Python C API exceptions: %s\n", e.what());
        throw e;
    }
}

PYBIND11_MODULE(_server, m)
{
    py::class_<Server>(m, "Server") //
        .def_static("getInstance", &Server::getInstance, py::return_value_policy::reference_internal);
}
