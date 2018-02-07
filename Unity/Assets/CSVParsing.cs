using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System.IO;

public class CSVParsing : MonoBehaviour
{

    public TextAsset csvFile; // Reference of CSV file
     private char lineSeperater = '\n'; // It defines line seperate character
    private char fieldSeperator = ','; // It defines field seperate chracter

    public float[] xData;
    public float[] yData;
    public float[] velocity;

    void Awake()
    {
        readData();
        
    }
    // Read data from CSV file
    private void readData()
    {
        Debug.Log("-");

        string[] records = csvFile.text.Split(lineSeperater);
        for (int j = 0; j < records.Length; j++)
        {
           
            string[] fields = records[j].Split(fieldSeperator);
           float[] value = new float[fields.Length];
            for (int i = 0; i < fields.Length; i++)
            {
                if(j == 2) Debug.Log(float.Parse(fields[i]));
                if(float.TryParse(fields[i],out value[i]))
                {
                    
                }
                else
                {
                    Debug.Log("Error!");
                }
                //value[i] = 6f;
                //value[i] = double.Parse(fields[i]);
                //contentArea.text += fields[i] + "\t";

            }
            if (j == 0) xData = value;
            if (j == 1) yData = value;
            if (j == 2) velocity = value;
            //contentArea.text += '\n';
        }
    }


    // Get path for given CSV file
    private static string getPath()
    {
#if UNITY_EDITOR
        return Application.dataPath;
#elif UNITY_ANDROID
return Application.persistentDataPath;// +fileName;
#elif UNITY_IPHONE
return GetiPhoneDocumentsPath();// +"/"+fileName;
#else
return Application.dataPath;// +"/"+ fileName;
#endif
    }
    // Get the path in iOS device
    private static string GetiPhoneDocumentsPath()
    {
        string path = Application.dataPath.Substring(0, Application.dataPath.Length - 5);
        path = path.Substring(0, path.LastIndexOf('/'));
        return path + "/Documents";
    }

}