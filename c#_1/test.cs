using UnityEngine;

public class test : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created

    private int Characterage = 19;
    public string Charactername = "Steve";
    bool FavoriteColorIsRed = true;
    int Combo = 0;
    int[] comboArray = new int[10];
    
    
   

    void Start()
    {
        Debug.Log("hello world");
        Debug.Log(Charactername);
        Debug.Log(Characterage);
       

        if (FavoriteColorIsRed)
        {
            Debug.Log(Charactername + "'s favorite color is red.");
        }
        else
        {
            Debug.Log(Charactername + "'s favorite color is not red");
        }
       
        int result = Add(1, 2);

        Debug.Log("The result of Add(1, 2) is: " + result);

        for (int i = 0; i < comboArray.Length; i++)
        {
            comboArray[i] = i + 1; 
        }
         for (int i = 0; i < comboArray.Length; i++)
        {
            Debug.Log("Combo count: " + comboArray[i]);
        }
        Combo = comboArray.Length; 
        Debug.Log($"Total Combo count is: {Combo}");



  
    }
  
    int Add(int a, int b)
    {
        return a + b;

    }
}
