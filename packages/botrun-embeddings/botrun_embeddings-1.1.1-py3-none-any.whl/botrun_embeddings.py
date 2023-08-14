#!/usr/bin/env python
# from botrun_embeddings import *
import glob
import heapq
import os

import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

sentence_transformer = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')


def encode_file(file_path, model=sentence_transformer):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    embeddings = model.encode(content)
    return embeddings


def create_embeddings(input_folder):
    txt_files = glob.glob(os.path.join(input_folder, '**/*_page_*.txt'), recursive=True)
    for txt_file in txt_files:
        current_folder = os.path.dirname(txt_file)
        file_base_name = os.path.splitext(os.path.basename(txt_file))[0]
        embeddings_file = os.path.join(current_folder, f"{file_base_name}.pt")
        if os.path.exists(embeddings_file):
            continue
        embeddings = encode_file(txt_file, sentence_transformer)
        torch.save(embeddings, embeddings_file)


def find_similar_files(query, folder_path, top_k=5):
    query_vector = sentence_transformer.encode([query])[0]
    similarity_scores = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pt'):
                pt_file = torch.load(os.path.join(root, file))
                similarity_score = cosine_similarity(query_vector.reshape(1, -1), pt_file.reshape(1, -1))[0][0]
                similarity_scores.append((similarity_score, os.path.join(root, file)))

    top_k_score_files = heapq.nlargest(top_k, similarity_scores)

    results = []

    for i, (score, file_path) in enumerate(top_k_score_files[:top_k]):
        result_str = f"Knowledgebase Top {i + 1} file: {file_path.replace('.pt', '.txt')}\n"
        result_str += f"Similarity score: {score}\n"
        with open(file_path.replace('.pt', '.txt'), 'r') as f:
            result_str += f"Content: {f.read()}\n"
        results.append(result_str)

    return '\n'.join(results)


if __name__ == '__main__':
    create_embeddings('users/cbh_cameo_tw/data')
    print(find_similar_files("主管的性別統計資料", 'users/cbh_cameo_tw/data', top_k=5))
