# Copyright (C) 2022 Cochise Ruhulessin # type: ignore
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import enum


class OrderProcessingMethod(str, enum.Enum):
    checkout = 'checkout'
    direct = 'direct'
    manual = 'manual'
    offsite = 'offsite'
    express = 'express'
    free = 'free'

    # Not documented
    none = ''
    wallet = 'wallet'
    payment_service_redirect = 'payment_service_redirect'