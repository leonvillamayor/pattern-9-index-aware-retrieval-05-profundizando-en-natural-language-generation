# Pseudocódigo del clasificador
for sentence in generated_response:
    label = classifier.predict(sentence, domain=my_domain)
    if label == "citation_worthy":
        sentence += f" [{best_matching_chunk_id}]"