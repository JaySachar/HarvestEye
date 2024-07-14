// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/archetypes/pinhole.fbs".

#include "pinhole.hpp"

#include "../collection_adapter_builtins.hpp"

namespace rerun::archetypes {}

namespace rerun {

    Result<std::vector<DataCell>> AsComponents<archetypes::Pinhole>::serialize(
        const archetypes::Pinhole& archetype
    ) {
        using namespace archetypes;
        std::vector<DataCell> cells;
        cells.reserve(4);

        {
            auto result = DataCell::from_loggable(archetype.image_from_camera);
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.resolution.has_value()) {
            auto result = DataCell::from_loggable(archetype.resolution.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.camera_xyz.has_value()) {
            auto result = DataCell::from_loggable(archetype.camera_xyz.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        {
            auto indicator = Pinhole::IndicatorComponent();
            auto result = DataCell::from_loggable(indicator);
            RR_RETURN_NOT_OK(result.error);
            cells.emplace_back(std::move(result.value));
        }

        return cells;
    }
} // namespace rerun
