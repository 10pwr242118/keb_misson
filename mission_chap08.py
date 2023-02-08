# day 05, 8.14

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

movie =  {titles: plots for titles,plots in zip(titles, plots)}