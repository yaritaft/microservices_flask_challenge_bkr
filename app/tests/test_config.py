import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.src.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config["SECRET_KEY"] is "my_precious")
        self.assertTrue(app.config["DEBUG"] is True)

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.TestingConfig")
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config["SECRET_KEY"] is "my_precious")
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(app.config["SQLALCHEMY_DATABASE_URI"] is not None)
        self.assertTrue("mytestingdb" in app.config["SQLALCHEMY_DATABASE_URI"])

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["DEBUG"] is False)


if __name__ == "__main__":
    unittest.main()
