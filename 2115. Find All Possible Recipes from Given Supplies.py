class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        all_recipes = []

        while True:
            intial_recipes = []
            n = len(recipes)
            if not n:
                return all_recipes

            for i in range(n):
                is_initial = True
                for ingridient in ingredients[i]:
                    if ingridient in recipes:
                        is_initial = False
                        break
                if is_initial:
                    intial_recipes.append(i)

            if not intial_recipes:
                return all_recipes

            added = 0
            for recipe in intial_recipes[::-1]:
                can_cook = True
                for ingredient in ingredients[recipe]:
                    if not ingredient in supplies:
                        can_cook = False
                        break
                if can_cook:
                    supplies.append(recipes[recipe])
                    all_recipes.append(recipes[recipe])
                    added += 1
                    recipes.pop(recipe)
                    ingredients.pop(recipe)

            if not added:
                return all_recipes


print(Solution().findAllRecipes(recipes = ["bread"],
                                ingredients = [["yeast","flour"]],
                                supplies = ["yeast","flour","corn"]))
print(Solution().findAllRecipes(recipes = ["bread","sandwich"],
                                ingredients = [["yeast","flour"],["bread","meat"]],
                                supplies = ["yeast","flour","meat"]))
print(Solution().findAllRecipes(recipes = ["bread","sandwich","burger"],
                                ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
                                supplies = ["yeast","flour","meat"]))
print(Solution().findAllRecipes(recipes = ["ju","fzjnm","x","e","zpmcz","h","q"],
                                ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],
                                supplies = ["f","hveml","cpivl","d"]))