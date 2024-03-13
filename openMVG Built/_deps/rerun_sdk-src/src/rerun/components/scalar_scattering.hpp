// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/components/scalar_scattering.fbs".

#pragma once

#include "../result.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class BooleanBuilder;
    class DataType;
} // namespace arrow

namespace rerun::components {
    /// **Component**: If true, a scalar will be shown as individual point in a scatter plot.
    struct ScalarScattering {
        bool scattered;

      public:
        ScalarScattering() = default;

        ScalarScattering(bool scattered_) : scattered(scattered_) {}

        ScalarScattering& operator=(bool scattered_) {
            scattered = scattered_;
            return *this;
        }
    };
} // namespace rerun::components

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<components::ScalarScattering> {
        static constexpr const char Name[] = "rerun.components.ScalarScattering";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::BooleanBuilder* builder, const components::ScalarScattering* elements,
            size_t num_elements
        );

        /// Serializes an array of `rerun::components::ScalarScattering` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::ScalarScattering* instances, size_t num_instances
        );
    };
} // namespace rerun