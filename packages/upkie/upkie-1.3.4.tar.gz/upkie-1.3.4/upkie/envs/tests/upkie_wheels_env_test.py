#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test UpkieWheelsEnv."""

import unittest

import posix_ipc

from envs import UpkieWheelsEnv

from envs.tests.mock_spine import MockSpine


class TestUpkieWheelsEnv(unittest.TestCase):
    def setUp(self):
        shm_name = "/vroum"
        shared_memory = posix_ipc.SharedMemory(
            shm_name, posix_ipc.O_RDWR | posix_ipc.O_CREAT, size=42
        )
        self.env = UpkieWheelsEnv(
            fall_pitch=1.0,
            frequency=100.0,
            shm_name=shm_name,
        )
        shared_memory.close_fd()
        self.env._spine = MockSpine()

    def test_reset(self):
        observation, info = self.env.reset()
        observation_dict = info["observation"]
        self.assertAlmostEqual(
            observation[1], observation_dict["wheel_odometry"]["position"]
        )
        self.assertGreaterEqual(observation_dict["number"], 1)


if __name__ == "__main__":
    unittest.main()
