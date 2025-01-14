# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Atlan Pte. Ltd.
from __future__ import annotations

from typing import Optional

from pydantic import Field

from pyatlan.model.core import AtlanObject


class AtlanImage(AtlanObject):
    id: Optional[str] = Field(description="Unique identifier (GUID) of the image.")
    version: Optional[str] = Field(description="TBC")
    created_at: Optional[int] = Field(
        description="Time at which the image was uploaded (epoch), in milliseconds."
    )
    updated_at: Optional[int] = Field(
        description="Time at which the image was last modified (epoch), in milliseconds."
    )
    file_name: Optional[str] = Field(
        description="Generated name of the image that was uploaded."
    )
    raw_name: Optional[str] = Field(
        description="Generated name of the image that was uploaded."
    )
    key: Optional[str] = Field(
        description="Generated name of the image that was uploaded."
    )
    extension: Optional[str] = Field(
        description="Filename extension for the image that was uploaded."
    )
    content_type: Optional[str] = Field(
        description="MIME type for the image that was uploaded."
    )
    file_size: Optional[str] = Field(
        description="Size of the image that was uploaded, in bytes."
    )
    is_encrypted: Optional[bool] = Field(
        description="Whether the image is encrypted (true) or not (false)."
    )
    redirect_url: Optional[str] = Field(description="TBC")
    is_uploaded: Optional[bool] = Field(description="TBC")
    uploaded_at: Optional[str] = Field(description="TBC")
    is_archived: Optional[bool] = Field(
        description="Whether the image has been archived (true) or is still actively available (false)."
    )
