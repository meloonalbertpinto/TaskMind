import re

class FileParser:
    @staticmethod
    def parse_vtt(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        clean_lines = [re.sub(r'<[^>]+>', '', l).strip() for l in lines 
                       if "-->" not in l and "WEBVTT" not in l and l.strip()]
        return " ".join(clean_lines)

    @staticmethod
    def parse_srt(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
        return " ".join(content.split())