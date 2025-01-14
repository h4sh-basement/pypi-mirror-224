use crate::utils::{
    errors::to_pyresult,
    reference::{RefMutContainer, RefMutOwner},
};
use crate::{deserialize_bytes, implement_type_conversion};
use prost::Message as ProstMessage;
use protobuf::Message as PbMessage;
use pyo3::{intern, prelude::*, pyclass::CompareOp, types::PyBytes};

use super::{conf_change_type::PyConfChangeType, conf_change_v2::PyConfChangeV2};

use raft::{
    eraftpb::ConfChange,
    prelude::{ConfChangeSingle, ConfChangeType, ConfChangeV2},
};

#[derive(Clone)]
#[pyclass(name = "ConfChange")]
pub struct PyConfChange {
    pub inner: RefMutOwner<ConfChange>,
}

#[derive(Clone)]
#[pyclass(name = "ConfChangeRef")]
pub struct PyConfChangeRef {
    pub inner: RefMutContainer<ConfChange>,
}

#[derive(FromPyObject)]
pub enum PyConfChangeMut<'p> {
    Owned(PyRefMut<'p, PyConfChange>),
    RefMut(PyConfChangeRef),
}

implement_type_conversion!(ConfChange, PyConfChangeMut);

pub fn format_confchange(cc: &ConfChange, py: Python) -> String {
    format!(
        "ConfChange {{ change_type: {change_type:?}, node_id: {node_id:?}, context: {context:?}, id: {id:?} }}",
        change_type = cc.get_change_type(),
        node_id = cc.get_node_id(),
        id = cc.get_id(),
        context = deserialize_bytes!(cc, "confchange_context_deserializer", context, py)
    )
}

#[pymethods]
impl PyConfChange {
    #[new]
    pub fn new() -> Self {
        PyConfChange {
            inner: RefMutOwner::new(ConfChange::new()),
        }
    }

    #[staticmethod]
    pub fn default() -> Self {
        PyConfChange {
            inner: RefMutOwner::new(ConfChange::default()),
        }
    }

    #[staticmethod]
    pub fn decode(v: &[u8]) -> PyResult<PyConfChange> {
        Ok(PyConfChange {
            inner: RefMutOwner::new(to_pyresult(ProstMessage::decode(v))?),
        })
    }

    pub fn make_ref(&mut self) -> PyConfChangeRef {
        PyConfChangeRef {
            inner: RefMutContainer::new(&mut self.inner),
        }
    }

    pub fn __repr__(&self, py: Python) -> String {
        format_confchange(&self.inner.inner, py)
    }

    pub fn __richcmp__(&self, py: Python, rhs: PyConfChangeMut, op: CompareOp) -> PyObject {
        let rhs: ConfChange = rhs.into();

        match op {
            CompareOp::Eq => (self.inner.inner == rhs).into_py(py),
            CompareOp::Ne => (self.inner.inner != rhs).into_py(py),
            _ => py.NotImplemented(),
        }
    }

    fn __getattr__(this: PyObject, py: Python, attr: &str) -> PyResult<PyObject> {
        let reference = this.call_method0(py, intern!(py, "make_ref"))?;
        reference.getattr(py, attr)
    }
}

#[pymethods]
impl PyConfChangeRef {
    pub fn __repr__(&self, py: Python) -> PyResult<String> {
        self.inner.map_as_ref(|inner| format_confchange(inner, py))
    }

    pub fn __richcmp__(
        &self,
        py: Python,
        rhs: PyConfChangeMut,
        op: CompareOp,
    ) -> PyResult<PyObject> {
        self.inner.map_as_ref(|inner| {
            let rhs: ConfChange = rhs.into();

            match op {
                CompareOp::Eq => (inner == &rhs).into_py(py),
                CompareOp::Ne => (inner != &rhs).into_py(py),
                _ => py.NotImplemented(),
            }
        })
    }

    pub fn clone(&mut self) -> PyResult<PyConfChange> {
        Ok(PyConfChange {
            inner: RefMutOwner::new(self.inner.map_as_ref(|inner| inner.clone())?),
        })
    }

    pub fn encode(&self, py: Python) -> PyResult<PyObject> {
        self.inner
            .map_as_ref(|inner| PyBytes::new(py, inner.encode_to_vec().as_slice()).into_py(py))
    }

    pub fn get_id(&self) -> PyResult<u64> {
        self.inner.map_as_ref(|inner| inner.get_id())
    }

    pub fn set_id(&mut self, v: u64) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.set_id(v))
    }

    pub fn clear_id(&mut self) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.clear_id())
    }

    pub fn get_node_id(&self) -> PyResult<u64> {
        self.inner.map_as_ref(|inner| inner.get_node_id())
    }

    pub fn set_node_id(&mut self, v: u64) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.set_node_id(v))
    }

    pub fn clear_node_id(&mut self) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.clear_node_id())
    }

    pub fn get_change_type(&self) -> PyResult<PyConfChangeType> {
        self.inner
            .map_as_ref(|inner| inner.get_change_type().into())
    }

    pub fn set_change_type(&mut self, v: &PyConfChangeType) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.set_change_type(v.0))
    }

    pub fn clear_change_type(&mut self) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.clear_change_type())
    }

    pub fn get_context(&self, py: Python) -> PyResult<Py<PyBytes>> {
        self.inner
            .map_as_ref(|inner| PyBytes::new(py, inner.get_context()).into())
    }

    pub fn set_context(&mut self, v: &PyAny) -> PyResult<()> {
        let context = v.extract::<Vec<u8>>()?;
        self.inner.map_as_mut(|inner| inner.set_context(context))
    }

    pub fn clear_context(&mut self) -> PyResult<()> {
        self.inner.map_as_mut(|inner| inner.clear_context())
    }
}

#[pymethods]
impl PyConfChangeRef {
    // This function could be implemented in Python by using `Decode`
    // and set properties one by one manually, but it is implemented here
    // to maintain concise code and assist in achieving better performance.
    pub fn merge_from_bytes(&mut self, bytes: &PyAny) -> PyResult<()> {
        let bytes = bytes.extract::<Vec<u8>>()?;

        self.inner
            .map_as_mut(|inner| inner.merge_from_bytes(bytes.as_slice()))
            .and_then(to_pyresult)
    }
}

#[pymethods]
impl PyConfChangeRef {
    pub fn as_v1(&mut self) -> PyResult<Option<PyConfChangeRef>> {
        self.inner.map_as_mut(|inner| {
            Some(PyConfChangeRef {
                inner: RefMutContainer::new_raw(inner),
            })
        })
    }

    // TODO: Apply COW to below method
    pub fn as_v2(&mut self) -> PyResult<PyConfChangeV2> {
        self.clone().unwrap().make_ref().into_v2()
    }

    pub fn into_v2(&mut self) -> PyResult<PyConfChangeV2> {
        self.inner.map_as_mut(|inner| {
            let mut cc = ConfChangeV2::default();
            let single = new_conf_change_single(inner.node_id, inner.get_change_type());
            cc.mut_changes().push(single);
            cc.set_context(inner.take_context());

            PyConfChangeV2 {
                inner: RefMutOwner::new(cc),
            }
        })
    }
}

/// Creates a `ConfChangeSingle`.
pub fn new_conf_change_single(node_id: u64, typ: ConfChangeType) -> ConfChangeSingle {
    let mut single = ConfChangeSingle {
        node_id,
        ..Default::default()
    };
    single.set_change_type(typ);
    single
}
