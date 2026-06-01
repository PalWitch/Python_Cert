from unittest import TestCase
from oop import Form, Dreieck, Kreis, Viereck, Parallelogramm 

class FormsTest(TestCase):

    def test_dreieck_type(self):
        d = Dreieck(0.3, 0.2, 0.1)
        self.assertIsInstance(d, Form)

    def test_dreieck_umfang_0(self):
        d = Dreieck(0.3, 0.2, 0.1)
        self.assertAlmostEqual(d.umfang(), 0.6)

    def test_dreieck_umfang_1(self):
        d = Dreieck(1, 12, 23)
        self.assertAlmostEqual(d.umfang(), 36)

    def test_dreieck_umfang_2(self):
        d = Dreieck(3, 3.0, 3)
        self.assertAlmostEqual(d.umfang(), 9.0)

    def test_dreieck_inhalt_0(self):
        d = Dreieck(1, 1, 1)
        self.assertAlmostEqual(d.inhalt(), 0.4330127018922193)

    def test_dreieck_inhalt_1(self):
        d = Dreieck(1, 1, 2 ** 0.5)
        self.assertAlmostEqual(d.inhalt(), 0.5)

    def test_dreieck_inhalt_2(self):
        d = Dreieck(3, 4, 5)
        self.assertAlmostEqual(d.inhalt(), 6)

    def test_dreieck_hat_90_grad_winkel_0(self):
        d = Dreieck(4, 3, 5)
        self.assertTrue(d.hat_90_grad_winkel())

    def test_dreieck_hat_90_grad_winkel_1(self):
        d = Dreieck(4, 3, 6)
        self.assertFalse(d.hat_90_grad_winkel())

    def test_dreieck_hat_90_grad_winkel_2(self):
        d = Dreieck(1, 1, 2 ** 0.5)
        self.assertTrue(d.hat_90_grad_winkel())

    def test_dreieck_hat_90_grad_winkel_3(self):
        d = Dreieck(1, 2 ** 0.5, 1)
        self.assertTrue(d.hat_90_grad_winkel())

    def test_kreis_type(self):
        k = Kreis(1)
        self.assertIsInstance(k, Form)

    def test_kreis_pi_0(self):
        self.assertTrue(hasattr(Kreis, 'PI'))

    def test_kreis_umfang_0(self):
        k = Kreis(1)
        self.assertAlmostEqual(k.umfang(), 6.2831853)

    def test_kreis_umfang_1(self):
        k = Kreis(0.5)
        self.assertAlmostEqual(k.umfang(), 3.14159265)

    def test_kreis_umfang_2(self):
        k = Kreis(15)
        self.assertAlmostEqual(k.umfang(), 94.2477796)

    def test_kreis_inhalt_0(self):
        k = Kreis(1)
        self.assertAlmostEqual(k.inhalt(), 3.14159265)

    def test_kreis_inhalt_1(self):
        k = Kreis(0.5)
        self.assertAlmostEqual(k.inhalt(), 0.785398163)

    def test_kreis_inhalt_2(self):
        k = Kreis(15)
        self.assertAlmostEqual(k.inhalt(), 706.85834705)

    def test_viereck_type(self):
        v = Viereck(1, 2, 3, 4)
        self.assertIsInstance(v, Form)

    def test_viereck_inhalt_fail_0(self):
        with self.assertRaises(NotImplementedError):
            v = Viereck(1, 2, 3, 4)
            v.inhalt()

    def test_viereck_umfang_0(self):
        v = Viereck(1, 2, 3, 4)
        self.assertAlmostEqual(v.umfang(), 10)

    def test_viereck_umfang_1(self):
        v = Viereck(1, 1, 1, 1)
        self.assertAlmostEqual(v.umfang(), 4)

    def test_parallelogramm_type(self):
        p = Parallelogramm(1, 2)
        self.assertIsInstance(p, Viereck)

    def test_parallelogramm_umfang_0(self):
        p = Parallelogramm(1, 2)
        self.assertAlmostEqual(p.umfang(), 6)

    def test_parallelogramm_inhalt_0(self):
        p = Parallelogramm(1, 2)
        self.assertAlmostEqual(p.inhalt(), 2)

    def test_parallelogramm_inhalt_1(self):
        p = Parallelogramm(1, 1)
        self.assertAlmostEqual(p.inhalt(), 1)

    def test_parallelogramm_inhalt_2(self):
        p = Parallelogramm(0.5, 0.5)
        self.assertAlmostEqual(p.inhalt(), .25)

    def test_form_inhalt_fail_0(self):
        with self.assertRaises(NotImplementedError):
            f = Form()
            f.inhalt()

    def test_form_umfang_fail_0(self):
        with self.assertRaises(NotImplementedError):
            f = Form()
            f.umfang()