class Joiner():
    @classmethod
    def left_outer_join_sections(self, left_collection, right_collection, join_condition):
        merged_sections = []

        for left_instance in left_collection:
            right_matching = [right_instance for right_instance in right_collection if join_condition(left_instance, right_instance)]

            merge_instance = left_instance.copy()

            if len(right_matching):
                relevant_right = right_matching[0]
                merge_instance.update(relevant_right)

            merged_sections.append(merge_instance)

        return merged_sections
