import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "docs" / "systematic-review" / "search"))

import local_filter as L  # noqa: E402
import rank  # noqa: E402
import zone2_lowcheck  # noqa: E402
import build_reading_pack as pack  # noqa: E402
import ai_scores  # noqa: E402


class LocalFilterTest(unittest.TestCase):
    def test_parametric_pinn_against_classical_solver_takes_route_f3(self):
        # "parametric" itself was missed by an earlier pattern; this guards that fix.
        title = "Learning the solution operator of parametric PDEs with physics-informed DeepONets"
        abstract = "Up to three orders of magnitude faster compared a conventional PDE solver."
        self.assertIn("F3", L.routes(title, abstract))

    def test_computational_carbon_takes_route_f1(self):
        self.assertIn("F1", L.routes("Carbon footprint of training Fourier neural operators", "We report carbon emissions."))

    def test_break_even_takes_route_f2(self):
        abstract = "A neural operator for partial differential equations breaks even after 400 queries."
        self.assertIn("F2", L.routes("Surrogates versus finite elements", abstract))

    def test_record_without_any_route_is_dropped(self):
        self.assertEqual(L.routes("Gaussian process regression for traffic counts", "No differential equations."), [])

    def test_hyphens_are_normalised(self):
        self.assertEqual(L.norm("Physics-Informed  Neural-Network"), "physics informed neural network")


class RankTest(unittest.TestCase):
    def test_building_energy_scores_below_computational_energy(self):
        # Known limit (search-log.md): a model name right next to "energy consumption" still counts as compute energy.
        building = {"title": "Office heating demand", "abstract": "We predict the energy consumption of an office building with a physics-informed neural network.",
                    "year": "2025", "type": "Journal article"}
        compute = {"title": "PINN training energy", "abstract": "Energy consumption of training on GPUs was measured.", "year": "2025", "type": "Journal article"}
        s_building, f_building = rank.score(building)
        s_compute, f_compute = rank.score(compute)
        self.assertLess(s_building, s_compute)
        self.assertFalse(f_building["strong"])
        self.assertTrue(f_compute["strong"])

    def test_low_tier_check_needs_classical_solver_and_cost_signal(self):
        self.assertTrue(zone2_lowcheck.passes("PINN surrogate", "Ten times faster than the finite element solver."))
        self.assertFalse(zone2_lowcheck.passes("PINN surrogate", "Ten times faster than a vanilla network."))



class ReadingPackTest(unittest.TestCase):
    def test_abstract_markup_is_stripped(self):
        raw = "<jats:p>Neural  solvers &amp; FEM</jats:p>"
        self.assertEqual(pack.clean_abstract(raw), "Neural solvers & FEM")

    def test_embedded_json_cannot_close_the_script_element(self):
        self.assertNotIn("</script", pack.safe_json({"abstract": "x </script><b>y"}))

    def test_author_line_shortens_long_lists(self):
        self.assertEqual(pack.author_line(["A. One", "B. Two", "C. Three"]), "A. One et al. (3 authors)")

    def test_reading_list_order_puts_cited_items_before_read_only_ones(self):
        def study(rl, total):
            return {"reading_list": rl, "id": rl or "x", "ai": {"C1_relevance": str(total)}}
        ordered = sorted([study("", 9), study("A", 7), study("opt", 8), study("12", 5), study("2", 9)], key=pack.list_order)
        self.assertEqual([s["reading_list"] for s in ordered], ["2", "12", "A", "opt", ""])


class AiScoresTest(unittest.TestCase):
    def test_every_selection_row_has_a_score(self):
        import csv
        path = Path(__file__).resolve().parents[1] / "docs" / "systematic-review" / "team-selection.csv"
        with open(path, encoding="utf-8", newline="") as f:
            ids = {row["id"] for row in csv.DictReader(f)}
        self.assertEqual(ids, set(ai_scores.SCORES))

    def test_rule_or_reading_list_selects(self):
        self.assertEqual(ai_scores.decision((1, 1, 0, 1, 2), "10"), "yes")
        self.assertEqual(ai_scores.decision((0, 1, 0, 0, 1), ""), "no")
        self.assertEqual(ai_scores.decision((0, 0, 0, 2, 0), ""), "yes")

if __name__ == "__main__":
    unittest.main()
