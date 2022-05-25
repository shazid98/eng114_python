from ..app_lib.budget_items_manager import BudgetItems


class TestBudgetItemsManager:

    budget_items_manager = BudgetItems()

    def test_items_empty_on_initialisation(self):
        assert bool(self.budget_items_manager.budget_items) is False

    def test_add_item_to_budget_list(self):
        self.budget_items_manager.add_budget_item("lunch", 5.50)
        assert self.budget_items_manager.budget_items["lunch"] == 5.50

    def test_budget_item_value_returned(self):
        assert self.budget_items_manager.return_budget_item_value('lunch') == 5.50

    def test_item_is_removed_from_budget_list(self):
        self.budget_items_manager.delete_budget_item("lunch")
        assert bool(self.budget_items_manager.budget_items) is False

