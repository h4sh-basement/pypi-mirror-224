use daft_dsl::Expr;

use crate::FileFormat;

#[derive(Debug)]
pub enum SinkInfo {
    OutputFileInfo(OutputFileInfo),
}

#[derive(Debug, Clone)]
pub struct OutputFileInfo {
    pub root_dir: String,
    pub file_format: FileFormat,
    pub partition_cols: Option<Vec<Expr>>,
    pub compression: Option<String>,
}

impl OutputFileInfo {
    pub fn new(
        root_dir: String,
        file_format: FileFormat,
        partition_cols: Option<Vec<Expr>>,
        compression: Option<String>,
    ) -> Self {
        Self {
            root_dir,
            file_format,
            partition_cols,
            compression,
        }
    }
}
