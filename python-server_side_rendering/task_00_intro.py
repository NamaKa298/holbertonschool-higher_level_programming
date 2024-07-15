import os

def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        print("Erreur : template n'est pas dans le bon format.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : attendees n'est pas dans le bon format.")
        return
    if template_content == '\0':
        print("Template is empty, no output files generated.")
        return
    if attendees =='\0':
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        invitation = template_content
        try:
            for placeholder, value in attendee.items():
                invitation = invitation.replace(f"{{{placeholder}}}", value if value is not None else "N/A")
            
            output_filename = f"output_{index}.txt"
            if os.path.exists(output_filename):
                print(f"Le fichier {output_filename} existe déjà, veuillez vérifier.")
                continue
            
            with open(output_filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Une erreur est survenue lors de la génération de l'invitation pour {attendee.get('name', 'N/A')}: {e}")
