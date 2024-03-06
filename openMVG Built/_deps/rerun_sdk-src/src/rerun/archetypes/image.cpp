// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/archetypes/image.fbs".

#include "image.hpp"

#include "../collection_adapter_builtins.hpp"

namespace rerun::archetypes {}

namespace rerun {

    Result<std::vector<DataCell>> AsComponents<archetypes::Image>::serialize(
        const archetypes::Image& archetype
    ) {
        using namespace archetypes;
        std::vector<DataCell> cells;
        cells.reserve(3);

        {
            auto result = DataCell::from_loggable(archetype.data);
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.draw_order.has_value()) {
            auto result = DataCell::from_loggable(archetype.draw_order.value());
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        {
            auto indicator = Image::IndicatorComponent();
            auto result = DataCell::from_loggable(indicator);
            RR_RETURN_NOT_OK(result.error);
            cells.emplace_back(std::move(result.value));
        }

        return cells;
    }
} // namespace rerun
