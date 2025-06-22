# TEXT-SUMMARIZATION

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SHARMI S

*DURATION*: 4 WEEKS 

*DOMAIN*: ARTIFICIAL INTELLIGENCE

***The Text Summarization Tool is a Python-based application developed to automatically condense long pieces of text into concise, meaningful summaries using Natural Language Processing (NLP) techniques. As digital content continues to grow rapidly, individuals and organizations often face the challenge of reading through extensive material to extract relevant information. This tool addresses that problem by summarizing lengthy articles, essays, reports, or any form of textual content into shorter versions while preserving the essential meaning and intent. The project leverages pre-trained transformer models provided by Hugging Face’s transformers library—specifically the facebook/bart-large-cnn model, which is widely recognized for its effectiveness in abstractive summarization tasks. Unlike extractive summarization that pulls exact sentences from the input, abstractive summarization understands the context and rewrites the key ideas in a more natural and human-like way.

The tool works by taking input text either manually through the terminal or from pasted content. It processes the text in manageable chunks to accommodate model limitations, ensuring that even long documents can be summarized without hitting token constraints. Internally, the tool intelligently calculates the best max_length for summaries based on input size to avoid performance warnings or undesired output verbosity. This is done by dynamically adjusting the max_length parameter, which helps the model generate summaries that are well-balanced, neither too short nor unnecessarily long. The use of token-count-aware logic ensures the output is clean and accurate even when summarizing very short or very long inputs.

From a technical perspective, the script initializes a summarization pipeline using Hugging Face’s transformer model, loads the input, and breaks it into segments that the model can handle. It then generates summaries for each chunk and combines them, finally limiting the total number of lines to ensure readability. The final output is presented in the terminal along with the original text, giving users a quick comparison between the source and the summary. Users don’t need advanced programming knowledge to use this tool; it runs entirely in the terminal with minimal setup. After installing dependencies like transformers and torch, users can start the summarization process by running a single Python script.

This tool has wide applications in education, journalism, research, and business. Students can use it to quickly understand textbook chapters or academic articles. Journalists can use it to scan press releases or lengthy reports, while researchers can summarize papers or data logs. Businesses can summarize meeting transcripts or customer feedback efficiently. Additionally, the tool sets the foundation for further development. It can be extended to support file inputs (like PDF or DOCX), provide a graphical user interface using Streamlit or Tkinter, or even be deployed as a web service.

In conclusion, the Text Summarization Tool showcases how modern NLP techniques can be practically applied to solve real-world problems. By automating the time-consuming task of summarizing large volumes of text, it not only improves productivity but also demonstrates the power of AI-driven language models. With growing demand for information processing and decision-making tools, such summarization solutions are becoming increasingly valuable in both personal and professional contexts.***

****OUTPUT****
![Image](https://github.com/user-attachments/assets/d5e91c45-b53b-406e-b9f8-87bf9b15c5fe)
