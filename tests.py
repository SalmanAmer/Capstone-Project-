import unittest
from unittest import result
import MysqlConnection
from datetime import datetime
import MainAlg
from kivy.uix.image import Image



class TestSQL(unittest.TestCase):
    
    def test_set_get_Theme(self):
        MysqlConnection.set_Theme(False)
        self.assertEqual(MysqlConnection.get_Theme(), 0, "Should be 0")
        MysqlConnection.set_Theme(True)
        self.assertEqual(MysqlConnection.get_Theme(), 1, "Should be 1")


    def test_add_get_actions_by_id(self):
        expected=('A', 'Good job! No letter mistakes found.')
        progressid=1
        progname="name"
        MysqlConnection.add_action_to_progress(progressid,'A',None, 'Good job! No letter mistakes found.',progname)
        result=MysqlConnection.get_Actions_by_id(progressid)
        result=result[0][1:-1]

        self.assertEqual(result, expected, f"Should be {expected}")
    
    def test_login_DB(self):
        expected =[(1, 'salman', 'amer', 'Salmana3335@gmail.com')]
        self.assertEqual(MysqlConnection.Log_in_DB('salman','amer'), expected, f"Should be {expected}")
        expected=[]
        self.assertEqual(MysqlConnection.Log_in_DB('saalman','amer'), expected, f"Should be {expected}")

    def test_create_account(self):
        expected=[("salman1","password","salman99@gmail.com")]
        MysqlConnection.create_account(expected[0][0],expected[0][1],expected[0][2])
        self.assertEqual([MysqlConnection.Log_in_DB('salman1','password')[0][1:]], expected, f"Should be {expected}")

    def test_create_get_progress(self):
        userid=2
        MysqlConnection.create_progress(2, 'learn', 'English', 'Beginner', 'Letters')  
        expected=('learn', 'English', 'Beginner', 'Letters')
        result=MysqlConnection.get_progresses(userid,"Letters")
        result=result[0][1:]
        self.assertEqual(result, expected, f"Should be {expected}")


    def test_Inc_get_Counter(self):
        progressid=17
        cnt= MysqlConnection.get_counter(progressid)    
        MysqlConnection.Counter_INC(progressid)
        incermented_cnt=MysqlConnection.get_counter(progressid)
        self.assertEqual(cnt+1, incermented_cnt, f"Should be {incermented_cnt}")



    def test_create_save_quiz(self):
        progressid =17
        level="Beginner"
        Group=1
        quizid= MysqlConnection.create_quiz(progressid,level,Group)
        MysqlConnection.delete_incomplete_quizes(quizid)
        result=MysqlConnection.get_progress_quizes(progressid)
        self.assertNotEqual(result[0][0],quizid,f"Should not be {quizid}")
        quizid= MysqlConnection.create_quiz(progressid,level,Group)
        grade=100
        MysqlConnection.save_quiz_grade(quizid,grade)
        result=MysqlConnection.get_progress_quizes(progressid)
        current_date = datetime.now().date()
        expected=(progressid,level,Group,grade,str(current_date))
        self.assertEqual(result[0][1:],expected,f"Should be {expected}")

    def test_add_get_action_quiz(self):
        progressid=17
        level="Beginner"
        Group=1
        quizid=MysqlConnection.create_quiz(progressid,level,Group)
        grade=100
        MysqlConnection.save_quiz_grade(quizid,grade)
        LW='A'
        image=None
        feedback='Good job! No letter mistakes found.'   
        MysqlConnection.add_action_to_quiz(progressid,quizid,LW,image,feedback) 
        result=MysqlConnection.get_Quiz_Actions(progressid)
        resultimg=MysqlConnection.get_Quiz_Actions_imgs(progressid)
        expected=(progressid,LW,feedback)
        self.assertEqual(result[0][2:],expected,f"Should be {expected}")
        self.assertEqual(resultimg[0][0],image,f"Should be {image}")

    def test_write_read_image_blob(self):
        image=MysqlConnection.read_blob_and_convert_to_image()
        try:
            MysqlConnection.write_image_to_blob(None,"image")
        except Exception:
            result=MysqlConnection.read_blob_and_convert_to_image()
            self.assertEqual(str(image),str(result),f"Should be {image}")


    def test_insert_read_delete_letters(self):
        image=MysqlConnection.read_blob_and_convert_to_image()
        MysqlConnection.insert_letter(image)
        result=MysqlConnection.read_all_letters()
        self.assertEqual(str(result[0]),str(image),f"Should be {image}")
        MysqlConnection.delete_all_letters()
        result=MysqlConnection.read_all_letters()
        self.assertEqual(result,[],f"Should be {[]}")

    def test_make_graph_insert_retieve(self):
        MainAlg.Make_Charts(16,"learn")
        expected= MysqlConnection.read_blob_and_convert_to_graph()
        self.assertTrue(isinstance(expected, Image),f"Should be kivy Image")

        

      
            

        



if __name__ == '__main__':
    unittest.main()
