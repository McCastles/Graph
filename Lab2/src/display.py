

# Out-sourced function from Widnow class
def display(window):
        
    is_visible = lambda node: \
        node[1] > window.focal if window.safe_mode else True
        
    # Background and aim
    window.screen.fill(window.BACKGROUND)
    window.pen.draw_aim(
        window.screen,
        window.WIDTH // 2, window.HEIGHT // 2,
        window.aim_radius)

    # Mark each figure with something to sort by
    figure_tuples = [
        ( figure, figure.center_depth(figure.nodes) )
        for figure in window.figures
    ]

    # Display figures according to their distance to the camera
    figure_tuples.sort (
        key=lambda tup: tup[1],
        reverse=True
    )

    # Display figure nodes, edges and/or facets
    for tup in figure_tuples:
        
        figure = tup[0]
        center_depth = tup[1]

        # Nodes
        if window.display_nodes:
            for node in figure.nodes:
                if is_visible(node):
                    x, y = figure.cast_3d_to_2d(
                        node, window.WIDTH, window.HEIGHT, window.focal)
                    window.pen.draw_node(window.screen, int(x), int(y))

        # Edges
        if window.display_edges:
            for (index_start, index_finish) in figure.edges:

                node_start = figure.nodes[index_start]
                node_finish = figure.nodes[index_finish]

                if is_visible(node_start) and is_visible(node_finish):

                    pair_start = figure.cast_3d_to_2d(
                        node_start,
                        window.WIDTH, window.HEIGHT, window.focal)

                    pair_finish = figure.cast_3d_to_2d(
                        node_finish,
                        window.WIDTH, window.HEIGHT, window.focal)
                        
                    window.pen.draw_edge(
                        window.screen,
                        pair_start,
                        pair_finish)

        # Facets
        if window.display_facets:
            
            # Find current facet nodes
            facets3D = [
                [ figure.nodes[i][:-1] for i in indexes ] 
                for indexes in window.facets_composition
            ]

            # Every facet has its color
            facets2D = []
            for facet3D, color in zip(
                facets3D, window.facets_colors):
                
                # Casting facets3D to 2D
                facet2D = []
                for node in facet3D:
                    pairxy = figure.cast_3d_to_2d(
                        node,
                        window.WIDTH, window.HEIGHT, window.focal)
                    
                    facet2D.append(pairxy)
                
                # Mark each facet2D with something to sort by
                facets2D.append({
                    'coords': facet2D,
                    'depth': figure.center_depth(facet3D),
                    'color': color
                })

            # Sorting by depth
            facets2D.sort(
                key=lambda slow: slow['depth'], reverse=True)

            # Draw facets according to the depth
            for facet2D in facets2D:
                window.pen.draw_facet(
                    window.screen,
                    facet2D['coords'], facet2D['color'])
