// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/blueprint/components/auto_layout.fbs".

#pragma once

#include "../../result.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class BooleanBuilder;
    class DataType;
} // namespace arrow

namespace rerun::blueprint::components {
    /// **Component**: Whether the viewport layout is determined automatically.
    ///
    /// Unstable. Used for the ongoing blueprint experimentations.
    struct AutoLayout {
        bool auto_layout;

      public:
        AutoLayout() = default;

        AutoLayout(bool auto_layout_) : auto_layout(auto_layout_) {}

        AutoLayout& operator=(bool auto_layout_) {
            auto_layout = auto_layout_;
            return *this;
        }
    };
} // namespace rerun::blueprint::components

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<blueprint::components::AutoLayout> {
        static constexpr const char Name[] = "rerun.blueprint.components.AutoLayout";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::BooleanBuilder* builder, const blueprint::components::AutoLayout* elements,
            size_t num_elements
        );

        /// Serializes an array of `rerun::blueprint:: components::AutoLayout` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::components::AutoLayout* instances, size_t num_instances
        );
    };
} // namespace rerun
