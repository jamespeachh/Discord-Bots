def format_character_info(info_list):
    lines = []
    
    if len(info_list) == 3 and isinstance(info_list[0], list) and isinstance(info_list[1], list) and isinstance(info_list[2], str):
        negative_effects = info_list[0][0]
        positive_effects = info_list[1][0]
        profession = info_list[2]
        lines.append("```")
        lines.append("Negative affects:")
        for i, effect in enumerate(negative_effects, start=1):
            lines.append(f"    {i}. {effect}")
        
        lines.append("Positive affects:")
        for i, effect in enumerate(positive_effects, start=1):
            lines.append(f"    {i}. {effect}")
        
        lines.append(f"Profession: {profession}")
        lines.append("```")
    else:
        return "Invalid input structure"

    formatted_string = "\n".join(lines)
    
    return formatted_string