class MailMerge:
    def __init__(self):
        self.REPLACE_WORD = '{name}'
        self.name_list = []

    def get_file(self, file_path_name_list, content_to_change):
        f""" Get file_path_name_list and mail_content and create mail_merge \n
            Carefully in checking your file path
        """
        with open(file_path_name_list) as name:
            content = name.readlines()
            for n in content:
                name_clear = n.strip()
                self.name_list.append(name_clear)
        with open(content_to_change) as mail:
            mail_content = mail.read()
            for new_word in self.name_list:
                new_mail = mail_content.replace(self.REPLACE_WORD, new_word)
                with open(f'letter for {new_word}', mode='w') as create_mail:
                    create_mail.write(new_mail)

