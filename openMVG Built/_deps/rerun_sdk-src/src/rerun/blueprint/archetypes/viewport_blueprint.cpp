// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/blueprint/archetypes/viewport_blueprint.fbs".

#include "viewport_blueprint.hpp"

#include "../../collection_adapter_builtins.hpp"

namespace rerun::blueprint::archetypes {}

namespace rerun {

    Result<std::vector<DataCell>> AsComponents<blueprint::archetypes::ViewportBlueprint>::serialize(
        const blueprint::archetypes::ViewportBlueprint& archetype
    ) {
        using namespace blueprint::archetypes;
        std::vector<DataCell> cells;
        cells.reserve(7);

        {
            auto result = DataCell::from_loggable(archetype.space_views);
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.layout.has_value()) {
            auto result = DataCell::from_loggable(archetype.layout.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.root_container.has_value()) {
            auto result = DataCell::from_loggable(archetype.root_container.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.maximized.has_value()) {
            auto result = DataCell::from_loggable(archetype.maximized.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.auto_layout.has_value()) {
            auto result = DataCell::from_loggable(archetype.auto_layout.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.auto_space_views.has_value()) {
            auto result = DataCell::from_loggable(archetype.auto_space_views.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        {
            auto indicator = ViewportBlueprint::IndicatorComponent();
            auto result = DataCell::from_loggable(indicator);
            RR_RETURN_NOT_OK(result.error);
            cells.emplace_back(std::move(result.value));
        }

        return cells;
    }
} // namespace rerun
