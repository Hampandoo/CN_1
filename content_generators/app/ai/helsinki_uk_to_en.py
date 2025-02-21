from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-uk-en'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate(text):
  tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

  token_length = tokens['input_ids'].shape[1]

  if token_length > 400:
    text_chunks = [text[i:i + 400] for i in range(0, len(text), 400)]  
  else:
    text_chunks = [text]

  translated_chunks = []
  for chunk in text_chunks:
    tokens_chunk = tokenizer(chunk, return_tensors="pt")
    translation = model.generate(**tokens_chunk)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    translated_chunks.append(translated_text)
  return " ".join(translated_chunks)