import asyncio
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

load_dotenv()

class TranscriptCollector:
    def __init__(self):
        self.reset()

    def reset(self):
        self.transcript_parts = []

    def add_part(self, part):
        self.transcript_parts.append(part)

    def get_full_transcript(self):
        return ' '.join(self.transcript_parts)

transcript_collector = TranscriptCollector()

async def get_transcript():
    try:
        config = DeepgramClientOptions(options={"keepalive": "true"})
        deepgram = DeepgramClient("", config)
        dg_connection = deepgram.listen.asynclive.v("1")

        # Flag to stop the loop when 'goodbye' is detected
        should_terminate = asyncio.Event()

        async def on_message(self, result, **kwargs):
            sentence = result.channel.alternatives[0].transcript

            if not result.speech_final:
                transcript_collector.add_part(sentence)
            else:
                transcript_collector.add_part(sentence)
                full_sentence = transcript_collector.get_full_transcript().strip()
                print(f"speaker: {full_sentence}")
                
                # Terminate if "goodbye" is in the finalized sentence
                if "goodbye" in full_sentence.lower():
                    should_terminate.set()

                transcript_collector.reset()

        async def on_error(self, error, **kwargs):
            print(f"\n\n{error}\n\n")

        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            endpointing=True
        )

        await dg_connection.start(options)

        microphone = Microphone(dg_connection.send)
        microphone.start()

        # Wait until "goodbye" is detected
        while microphone.is_active() and not should_terminate.is_set():
            await asyncio.sleep(0.5)

        microphone.finish()
        await dg_connection.finish()

        print("------------------------------------------------------------------")


    except Exception as e:
        print(f"Could not open socket: {e}")
        return

if __name__ == "__main__":
    asyncio.run(get_transcript())
