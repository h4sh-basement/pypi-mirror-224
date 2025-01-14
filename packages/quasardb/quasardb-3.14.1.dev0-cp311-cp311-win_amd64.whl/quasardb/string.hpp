/*
 *
 * Official Python API
 *
 * Copyright (c) 2009-2023, quasardb SAS. All rights reserved.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *    * Redistributions of source code must retain the above copyright
 *      notice, this list of conditions and the following disclaimer.
 *    * Redistributions in binary form must reproduce the above copyright
 *      notice, this list of conditions and the following disclaimer in the
 *      documentation and/or other materials provided with the distribution.
 *    * Neither the name of quasardb nor the names of its contributors may
 *      be used to endorse or promote products derived from this software
 *      without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY QUASARDB AND CONTRIBUTORS ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
#pragma once

#include "entry.hpp"
#include <qdb/string.h>
#include "convert/value.hpp"

namespace qdb
{
namespace py = pybind11;

class string_entry : public expirable_entry
{
public:
    string_entry(handle_ptr h, std::string a) noexcept
        : expirable_entry{h, a}
    {}

private:
    py::str convert_and_release_content(const char * content, qdb_size_t content_length)
    {
        return convert_and_release_content(qdb_string_t{content, content_length});
    }

    py::str convert_and_release_content(qdb_string_t x)
    {
        if (x.data == nullptr || x.length == 0)
        {
            return py::str{};
        }

        py::str ret = qdb::convert::value<qdb_string_t, py::str>(x);

        qdb_release(*_handle, x.data);
        return ret;
    }

public:
    py::str get()
    {
        const char * content      = nullptr;
        qdb_size_t content_length = 0;

        qdb::qdb_throw_if_error(
            *_handle, qdb_string_get(*_handle, _alias.c_str(), &content, &content_length));

        return convert_and_release_content(content, content_length);
    }

    void put(const std::string & data)
    {
        qdb::qdb_throw_if_error(*_handle,
            qdb_string_put(*_handle, _alias.c_str(), data.data(), data.size(), qdb_time_t{0}));
    }

    void update(const std::string & data,
        std::chrono::system_clock::time_point expiry = std::chrono::system_clock::time_point{})
    {
        qdb::qdb_throw_if_error(*_handle,
            qdb_string_update(*_handle, _alias.c_str(), data.data(), data.size(), qdb_time_t{0}));
    }

    void remove_if(const std::string & comparand)
    {
        qdb::qdb_throw_if_error(*_handle,
            qdb_string_remove_if(*_handle, _alias.c_str(), comparand.data(), comparand.size()));
    }

    py::str get_and_remove()
    {
        const char * content      = nullptr;
        qdb_size_t content_length = 0;

        qdb::qdb_throw_if_error(
            *_handle, qdb_string_get_and_remove(*_handle, _alias.c_str(), &content, &content_length));

        return convert_and_release_content(content, content_length);
    }

    py::str get_and_update(const std::string & data)
    {
        const char * content      = nullptr;
        qdb_size_t content_length = 0;

        qdb::qdb_throw_if_error(
            *_handle, qdb_string_get_and_update(*_handle, _alias.c_str(), data.data(), data.size(),
                          qdb_time_t{0}, &content, &content_length));

        return convert_and_release_content(content, content_length);
    }

    py::str compare_and_swap(const std::string & new_value, const std::string & comparand)
    {
        const char * content      = nullptr;
        qdb_size_t content_length = 0;

        qdb_error_t err =
            qdb_string_compare_and_swap(*_handle, _alias.c_str(), new_value.data(), new_value.size(),
                comparand.data(), comparand.size(), qdb_time_t{0}, &content, &content_length);

        // we don't want to throw on "unmatching content", so we don't use the qdb::qdb_throw_if_error
        // function
        if (QDB_FAILURE(err))
        {
            qdb_throw_if_error(*_handle, err);
        }

        return convert_and_release_content(content, content_length);
    }
};

template <typename Module>
static inline void register_string(Module & m)
{
    namespace py = pybind11;

    py::class_<qdb::string_entry, qdb::expirable_entry>(m, "String") //
        .def(py::init<qdb::handle_ptr, std::string>())               //
        .def("get", &qdb::string_entry::get)                         //
        .def("put", &qdb::string_entry::put, py::arg("data"))        //
        .def("update", &qdb::string_entry::update, py::arg("data"),
            py::arg("expiry") = std::chrono::system_clock::time_point{})       //
        .def("remove_if", &qdb::string_entry::remove_if, py::arg("comparand")) //
        .def("get_and_remove", &qdb::string_entry::get_and_remove)             //
        .def("get_and_update", &qdb::string_entry::get_and_update,             //
            py::arg("data"))                                                   //
        .def("compare_and_swap", &qdb::string_entry::compare_and_swap,         //
            py::arg("new_content"), py::arg("comparand"));                     //
}

} // namespace qdb
