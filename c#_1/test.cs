using UnityEngine;

public class test : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created

 private int Characterage = 19;
 public string Charactername = "Steve";
 bool FavoriteColorIsRed = true;
 int Combo = 0;
 int Add(int a, int b,)

    void Start()
    {
        Debug.Log("hello world");
        Debug.Log(Charactername);
        Debug.Log(Characterage);

        if (FavoriteColorIsRed)
        {
            Debug.Log(Charactername + "Steve's favorite color is red.");
        }
        else
        {
            Debug.Log(Charactername + "Steve's favorite color is not red");
        }
        
        {
            return a + b;
        }
        int result = Add(1, 2);
        Debug.Log(result);



  
    }
    void Update()
    { if (Combo < 10)
      {
        Debug.Log("Combo count: " + Combo);
        Combo++;
      }
    }
}
