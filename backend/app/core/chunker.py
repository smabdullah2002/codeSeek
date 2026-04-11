def chunk_code(content:str, file_path:str):
    lines= content.split("\n")
    chunks = []
    chunk_size=20 #lines per chunk
    
    for i in range(0, len(lines), chunk_size):
        chunk_lines= lines[i:i+chunk_size]
        chunk_text= "\n".join(chunk_lines)
        
        chunks.append({
            "file_path": file_path,
            "chunk_id": f"{file_path}_{i}",
            "chunk_type": "block",
            "name": None,
            "content": chunk_text,
            "metadata": {"language": "python"}
        })
    return chunks