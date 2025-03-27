using UnityEngine;

public class MenuButtons : MonoBehaviour
{
    public void onStartGameButtonClicked()
    {
        Debug.Log("Game Start");
    }

    private bool isPaused = false;


    public void TogglePause()
    {
        isPaused = !isPaused;
        Time.timeScale = isPaused ? 0 : 1;
        if (Time.timeScale == 1)
        {
            Debug.Log("Unpaused");
        }
        else
        {
            Debug.Log("pause");
        }
    }
}
