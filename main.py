import asyncio  

from dotenv import load_dotenv  
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm  
from livekit.agents.voice_assistant import VoiceAssistant  
from livekit.plugins import openai, silero  

load_dotenv()


# Main function defining the behavior of the voice assistant
async def entrypoint(ctx: JobContext):
    # Set up initial chat context with system-level instructions
    initial_ctx = llm.ChatContext().append(
        role="system",  # Define the assistant's role as "system"
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronounceable punctuation."
        ),
    )

    # Connect to the room and subscribe to audio-only streams
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Create a VoiceAssistant instance with required plugins and context
    assitant = VoiceAssistant(
        vad=silero.VAD.load(),  
        stt=openai.STT(), 
        llm=openai.LLM(),  
        tts=openai.TTS(),  
        chat_ctx=initial_ctx,  
    )

    # Start the assistant and attach it to the connected room
    assitant.start(ctx.room)

    # Pause for 1 second before speaking
    await asyncio.sleep(1)

    # The assistant speaks a greeting to the user, allowing interruptions during playback
    await assitant.say("Hey, how can I help you today!", allow_interruptions=True)


# Entry point for the application
if __name__ == "__main__":
    # Run the LiveKit application with the specified entrypoint function
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
