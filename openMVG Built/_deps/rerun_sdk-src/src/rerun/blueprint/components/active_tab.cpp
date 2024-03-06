// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/blueprint/components/active_tab.fbs".

#include "active_tab.hpp"

#include "../../datatypes/entity_path.hpp"

#include <arrow/builder.h>
#include <arrow/type_fwd.h>

namespace rerun::blueprint::components {}

namespace rerun {
    const std::shared_ptr<arrow::DataType>&
        Loggable<blueprint::components::ActiveTab>::arrow_datatype() {
        static const auto datatype = Loggable<rerun::datatypes::EntityPath>::arrow_datatype();
        return datatype;
    }

    rerun::Error Loggable<blueprint::components::ActiveTab>::fill_arrow_array_builder(
        arrow::StringBuilder* builder, const blueprint::components::ActiveTab* elements,
        size_t num_elements
    ) {
        static_assert(
            sizeof(rerun::datatypes::EntityPath) == sizeof(blueprint::components::ActiveTab)
        );
        RR_RETURN_NOT_OK(Loggable<rerun::datatypes::EntityPath>::fill_arrow_array_builder(
            builder,
            reinterpret_cast<const rerun::datatypes::EntityPath*>(elements),
            num_elements
        ));

        return Error::ok();
    }

    Result<std::shared_ptr<arrow::Array>> Loggable<blueprint::components::ActiveTab>::to_arrow(
        const blueprint::components::ActiveTab* instances, size_t num_instances
    ) {
        // TODO(andreas): Allow configuring the memory pool.
        arrow::MemoryPool* pool = arrow::default_memory_pool();
        auto datatype = arrow_datatype();

        ARROW_ASSIGN_OR_RAISE(auto builder, arrow::MakeBuilder(datatype, pool))
        if (instances && num_instances > 0) {
            RR_RETURN_NOT_OK(Loggable<blueprint::components::ActiveTab>::fill_arrow_array_builder(
                static_cast<arrow::StringBuilder*>(builder.get()),
                instances,
                num_instances
            ));
        }
        std::shared_ptr<arrow::Array> array;
        ARROW_RETURN_NOT_OK(builder->Finish(&array));
        return array;
    }
} // namespace rerun
