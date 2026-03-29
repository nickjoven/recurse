//! Schema definitions for the recurse ontology DAG.
//!
//! Three schemas:
//! - `ontology_node`: a concept in the algebraic vocabulary (Levels 0-3)
//! - `prediction`: a numerical prediction derived from the ontology (Level 4 leaves)
//! - `observation`: a measured value from external data (Phase 2+)

use canon_d::{FieldKind, Schema};

/// Schema for algebraic ontology nodes (Levels 0-3).
///
/// Identity: (level, slug) — "mediant" at level 0 is one node,
/// regardless of how many times it's seeded. Same canonical bytes
/// produce the same CID across repos.
pub fn ontology_node_schema() -> Schema {
    Schema::new("ontology_node", 1)
        .identity("level", FieldKind::String)
        .identity("slug", FieldKind::String)
        .required("name", FieldKind::String)
        .required("description", FieldKind::String)
        .optional("symbol", FieldKind::String)
        .optional("tags", FieldKind::List(Box::new(FieldKind::String)))
}

/// Schema for prediction leaves (Level 4).
///
/// Identity: (slug, predicted_value) — a specific prediction is one node.
/// The derivation chain (parents) traces back through the ontology to
/// the four Level 0 primitives.
pub fn prediction_schema() -> Schema {
    Schema::new("prediction", 1)
        .identity("slug", FieldKind::String)
        .identity("predicted_value", FieldKind::String)
        .required("name", FieldKind::String)
        .required("description", FieldKind::String)
        .required("quantity", FieldKind::String)
        .optional("uncertainty", FieldKind::String)
        .optional("source_derivation", FieldKind::String)
        .optional("testable_by", FieldKind::String)
}

/// Schema for observation leaves (Phase 2+).
///
/// Identity: (source, quantity) — one measurement from one source.
/// Same star sown twice produces same CID.
pub fn observation_schema() -> Schema {
    Schema::new("observation", 1)
        .identity("source", FieldKind::String)
        .identity("quantity", FieldKind::String)
        .required("value", FieldKind::String)
        .required("uncertainty", FieldKind::String)
        .optional("arxiv_id", FieldKind::String)
        .optional("catalog", FieldKind::String)
        .optional("stern_brocot_path", FieldKind::String)
        .optional("farey_address", FieldKind::String)
}
